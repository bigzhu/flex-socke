# -*- coding:UTF-8 -*-

from insert_ import insert
from insert_ import insertLog
from distri import insertDistriLog
from update_ import update
from distri import getDistriInfo
from public import getOperType
from public import addZero
import pool
from oracle import Oracle
from exp import Warning_
def instanceTax(oracle, **args):
    '''实例化,上架 distri_id, oper_staff_id, tax_begin_nbr, tax_end_nbr'''

    for k, v in args.items():
            exec "%s = '%s'"%(k,v)
    distri_info = getDistriInfo(oracle, distri_id)
    args['tax_code'] = distri_info['tax_code']
            
    hold_staff_id = distri_info['staff_id']
    args['hold_staff_id'] = hold_staff_id

    if(str(hold_staff_id)!= str(oper_staff_id)):
        raise Exception,'发票是工号%s的,只有本人才能对自己的发票上架'%hold_staff_id

    args['hold_tax_begin_nbr'] = distri_info['tax_begin_nbr']
    args['hold_tax_end_nbr'] = distri_info['tax_end_nbr']
    tax_type = getOperType(tax_begin_nbr, tax_end_nbr,
    distri_info['tax_begin_nbr'], distri_info['tax_end_nbr'])
    args['tax_type'] = tax_type
    if(tax_type == 'a'):
        allInstance(oracle, **args)
    #else:
    #    partDistri(oracle, **args)
def allInstance(oracle, **args):
    '''全部上架'''
    for k, v in args.items():
            exec "%s = '%s'"%(k,v)

    state = 'instance'
    update_dic = {'state':state,'state_date':'/sysdate'}
    where_dic = {'distri_id':distri_id}
    update(oracle, 'distri', update_dic, where_dic, "and state in('in','hold')")
    insertDistriLog(oracle = oracle, distri_id = distri_id, oper_staff_id = oper_staff_id, oper = 'instance', state = state)

    #先插入一条
    dic = {}
    pool_id = pool.getNextVal(oracle)
    dic['pool_id'] = pool_id
    dic['distri_id'] = distri_id
    dic['tax_code'] = tax_code
    dic['tax_nbr'] = tax_begin_nbr
    #dic['sys_type'] = 'B'
    dic['state'] = 'instance'
    dic['state_date'] = '/sysdate'
    dic['staff_id'] = oper_staff_id
    insert(oracle, 'pool', dic)

    must_instance_count =  int(tax_end_nbr)-int(tax_begin_nbr)+1
    if(hold_tax_begin_nbr!= hold_tax_end_nbr):

        length = len(hold_tax_begin_nbr)
        tax_nbr_list = []
        sql = '''	 insert into pool             
            		   (pool_id,                    
            		    distri_id,                  
            		    tax_code,                   
            		    tax_nbr,                    
            		    state,                      
            		    state_date,                 
            		    staff_id,                   
            		    sys_type)                
            		   (select pool_seq.nextval,        
            		           distri_id,           
            		           tax_code,            
            		           :tax_nbr,             
            		           state,               
            		           state_date,          
            		           staff_id,            
            		           sys_type            
            		      from  pool    
            		     where pool_id = %s)   '''%pool_id
        if(int(hold_tax_end_nbr)-int(hold_tax_begin_nbr)>100000):
            raise Warning_, '一次上架记录数有%s条,业务不允许,请下发拆分小于10W再上架'%(int(hold_tax_end_nbr)-int(hold_tax_begin_nbr))

        for i in range(int(hold_tax_begin_nbr)+1, int(hold_tax_end_nbr)+1):
            tax_nbr = addZero(length, i)
            dic = {'tax_nbr':tax_nbr}
            tax_nbr_list.append(dic)
        if(len(tax_nbr_list)>100000):
            raise Warning_, '一次上架记录数有%s条,业务不允许,请下发拆分小于10W再上架'
        if(len(tax_nbr_list)>50000):
            row_count = oracle.executemany(sql, tax_nbr_list[:50000])
            row_count+= oracle.executemany(sql, tax_nbr_list[50000:])
        else:
            row_count = oracle.executemany(sql, tax_nbr_list)
        if(row_count!= must_instance_count-1):
            raise Exception, '未能正确上架 distri_id = %s,应上架%s,实际只上了%s,数据发生变动,请重新查'%(distri_id, must_instance_count, row_count+1)

    where_dic = {'tax_code':tax_code, 'distri_id':distri_id, 'state':'instance', 'staff_id':oper_staff_id}
    and_the = "and to_number(tax_nbr)> = to_number('%s') and to_number(tax_nbr)< = to_number('%s')"%(tax_begin_nbr, tax_end_nbr)
    add_infos = {'oper':'instance'}
    add_infos['oper_staff_id'] = oper_staff_id
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'pool', where_dic, add_infos, and_the, must_instance_count)

def test_instanceTax(oracle):
    instanceTax(oracle, distri_id = 1203, oper_staff_id = 22, staff_id = 22, tax_begin_nbr = '00001', tax_end_nbr = '50000')

if __name__ == "__main__":
    from oracle import Oracle
    oracle = Oracle()
    test_instanceTax(oracle)
    oracle.commit()
