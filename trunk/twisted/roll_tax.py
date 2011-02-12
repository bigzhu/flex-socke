# -*- coding:UTF-8 -*-
''' 发票回滚 '''
from oracle import Oracle
from pool import selectPool
from datetime import datetime
from insert_ import insertLog

def roll(oracle, **args):
    ''' 发票回滚
        tax_code
        tax_nbr
        oper_staff_id
        remark
    '''
    sql = '''update pool p
                           set p.state = 'instance', p.state_date = sysdate
                         where p.tax_code = :tax_code
                           and p.tax_nbr = :tax_nbr
                           and p.state not in ('instance')
                        '''
    dic_tmp = {}
    dic_tmp['tax_code'] = args['tax_code']
    dic_tmp['tax_nbr'] = args['tax_nbr']
    row_count = oracle.execute(sql,dic_tmp)
    if(row_count !=  1):
        raise Exception, '给出条件未能找到可以回滚的发票记录;update pool %s 条记录'%row_count
    #取出 pool_id 顺便再次检查其是否更新成功
    select_colums = ['pool_id',]
    dic_tmp['state'] = 'instance'
    pool_id = selectPool(oracle, select_colums, dic_tmp)
    if(pool_id ==  None):
        raise Exception, '给出条件未能找到可以回滚的发票记录;update pool 失败'
    if(len(pool_id) !=  1):
        raise Exception, '状态同时为instance的记录有%s条'%len(pool_id)
    #根据pool_id 插入 pool_log表
    where_dic = {}
    where_dic['pool_id'] = pool_id[0]['pool_id']
    add_infos = {'oper':'roll'}
    add_infos['oper_staff_id'] = args['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'pool', where_dic, add_infos)

def test_rollTax():
    oracle = Oracle()
    roll(oracle, tax_code = '1234567', tax_nbr = '100204', oper_staff_id = 22)
    oracle.commit()

if __name__ ==  "__main__":
    test_rollTax()
