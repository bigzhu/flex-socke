# -*- coding:UTF-8 -*-
from select_ import select
from insert_ import insert
from insert_ import insertLog
from exp import Warning_
from types import StringType
from types import UnicodeType

from staff import upperLevel
from update_ import update


from public import addZero
from public import getOperType
from twisted.python import log 

def getStaffId(oracle, select_colums,where_dic):
    ''' 取得当前持有这个发票资源的工号 '''
    sql = ' from distri '
    select_result = select(oracle, select_colums,sql,where_dic)
    distri_id = where_dic['distri_id']
    if(select_result ==  None):
        raise Exception('根据distri_id = %s 找不到发票持有者'%distri_id)
    return select_result
def getNextVal(oracle):
    '''获得最新的distri_id'''
    sql = ' select distri_seq.nextval from dual '
    select_result = oracle.execute(sql)
    for select_info in select_result:
        return str(select_info[0]); 
def checkIfExist(oracle, **args):
    '''检查号段是否重叠'''
    select_colums = ['distri_id', 'tax_code', 'tax_begin_nbr', 'tax_end_nbr', 'staff_id']

    sql =  '''
              from distri
             where 1 = 1
               and tax_code in (:tax_code)
               and ((to_number(tax_begin_nbr) = to_number(:tax_begin_nbr) or
                   to_number(tax_end_nbr) = to_number(:tax_begin_nbr) or
                   to_number(tax_end_nbr) = to_number(:tax_end_nbr) or
                   to_number(tax_begin_nbr) = to_number(:tax_end_nbr)) or
                   (to_number(tax_begin_nbr) > to_number(:tax_begin_nbr) and
                   to_number(tax_end_nbr) < to_number(:tax_end_nbr)) or
                   (to_number(tax_begin_nbr) < to_number(:tax_begin_nbr) and
                   to_number(tax_end_nbr) < to_number(:tax_end_nbr) and
                   to_number(tax_end_nbr) > to_number(:tax_begin_nbr)) or
                   (to_number(tax_begin_nbr) > to_number(:tax_begin_nbr) and
                   to_number(tax_end_nbr) > to_number(:tax_end_nbr) and
                   to_number(tax_begin_nbr) < to_number(:tax_end_nbr)) or
                   (to_number(tax_begin_nbr) < to_number(:tax_begin_nbr) and
                   to_number(tax_end_nbr) > to_number(:tax_end_nbr)))
               and state in ('instance','hold','in','inFromCRM')
    '''

    select_info = select(oracle, select_colums, sql, bind_dic = args)

    if(select_info!= None):
        select_info = select_info[0]
        return '号段有重叠,已存在发票代码:%s 开始号码:%s,结束号码:%s,属于工号%s'%(select_info['tax_code'], select_info['tax_begin_nbr'], select_info['tax_end_nbr'], select_info['staff_id'])
    else:
        return "0"

'''
    select_result = oracle.execute(sql, args)
    for select_info in select_result:
        print select_info; 
        raise Warning_, '号段有重叠,已存在开始号码:%s,结束号码:%s,属于工号%s'%(select_info[2], select_info[3], select_info[4])
        '''
def addDistri(oracle, **args):
    result = checkIfExist(oracle, tax_code = args['tax_code'], tax_begin_nbr = args['tax_begin_nbr'], tax_end_nbr = args['tax_end_nbr'])
    if(result != "0"):
        raise Warning_, result
    

    dic = {}
    dic['distri_id'] = getNextVal(oracle)
    dic['parent_distri_id'] = '-1'
    dic['tax_code'] = args['tax_code']
    dic['tax_begin_nbr'] = args['tax_begin_nbr']
    dic['tax_end_nbr'] = args['tax_end_nbr']
    dic['sys_type'] = 'B'
    dic['state'] = 'in'
    dic['state_date'] = '/sysdate'
    dic['staff_id'] = args['staff_id']
    insert(oracle, 'distri', dic)

    where_dic = {}
    where_dic['distri_id'] = dic['distri_id']
    add_infos = {'oper':'add'}
    add_infos['oper_staff_id'] = args['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'distri', where_dic, add_infos)
def getDistriInfo(oracle, distri_id):
    '''获取持有发票的distri信息'''
    select_colums = ['staff_id', 'tax_begin_nbr', 'tax_end_nbr', 'tax_code']
    where_dic = {}
    where_dic['distri_id'] = distri_id
    #where_dic['state'] = 'hold'

    select_result = getStaffId(oracle, select_colums, where_dic)
    return select_result[0]
def checkBeginEndNbr(tax_begin_nbr, tax_end_nbr, hold_tax_begin_nbr, hold_tax_end_nbr):
    '''检查指定的发票号段是否合法'''
    if(tax_begin_nbr == None):
        raise Exception,'不能仅指定结束号码 = %s,而不指定开始号码 = %s'%(tax_end_nbr, tax_begin_nbr)
    if(tax_end_nbr == None):
        raise Exception,'不能仅指定开始号码 = %s,而不指定结束号码 = %s'%(tax_begin_nbr, tax_end_nbr)
    if(int(tax_begin_nbr)<int(hold_tax_begin_nbr)):
        raise Exception,'要回收开始号码%s,比持有的开始号码%s还要小,非法数据'%(tax_begin_nbr, hold_tax_begin_nbr)
    if(int(tax_end_nbr)>int(hold_tax_end_nbr)):
        raise Exception,'要回收结束号码%s,比持有的结束号码%s还要大,非法数据'%(tax_end_nbr, hold_tax_end_nbr)
def distriTax(oracle, **args):
    '''下发发票
		distri_id;
		staff_id;
		tax_begin_nbr;
		tax_end_nbr;
		tax_code;
		oper_staff_id;
                '''
#def insertDistriLog(oracle, distri_id, oper_staff_id, oper, state):
def insertDistriLog(oracle, **args):
    '''日志记录'''
    where_dic = {}
    where_dic['distri_id'] = args['distri_id']
    add_infos = {'oper':args['oper']}
    add_infos['oper_staff_id'] = args['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'distri', where_dic, add_infos)
def insertDistriAsSplit(oracle, new_distri_id, distri_id, staff_id, tax_begin_nbr = 'tax_begin_nbr', tax_end_nbr = 'tax_end_nbr'):
    '''向distri插入新的记录,用于拆分'''
    dic = {}
    dic['new_distri_id'] = new_distri_id
    dic['distri_id'] = distri_id
    dic['staff_id'] = staff_id

    if(tax_begin_nbr!= 'tax_begin_nbr'):
        dic['tax_begin_nbr'] = tax_begin_nbr
        tax_begin_nbr = ':tax_begin_nbr'
    if(tax_end_nbr!= 'tax_end_nbr'):
        dic['tax_end_nbr'] = tax_end_nbr
        tax_end_nbr = ':tax_end_nbr'
    sql = '''
        insert
        into distri
          (
            distri_id,
            parent_distri_id,
            tax_code,
            tax_begin_nbr,
            tax_end_nbr,
            bss_org_id,
            sys_type,
            state,
            state_date,
            staff_id
          )
        select 
            :new_distri_id,
            distri_id,
            tax_code,
            %s,
            %s,
            null,
            sys_type,
            'hold',
            sysdate,
            :staff_id
        from distri where distri_id = :distri_id
        '''%(tax_begin_nbr, tax_end_nbr)
    row_count = oracle.execute(sql, dic)
    if(row_count !=  1):
        raise Exception, '未能生成新的distri记录 %s 条记录 distri_id = %s'%(row_count,distri_id)




def test_checkIfExist(oracle):
    print checkIfExist(oracle, tax_code = '1', tax_begin_nbr = '1', tax_end_nbr = '1')
def test_getStaffId(oracle):
    select_colums = ['staff_id']
    where_dic = {"distri_id":"1111",'state':'a'}
    print getStaffId(oracle,select_colums,where_dic)
def test_addDistri(oracle):
    addDistri(oracle, tax_code = 'bigzhu', tax_begin_nbr = '001', tax_end_nbr = '999', staff_id = 71, oper_staff_id = 22)

def distriTax(oracle, **args):
    '''发票下发 staff_id, oper_staff_id  distri_id  tax_begin_nbr  tax_end_nbr '''
    for k, v in args.items():
        exec "%s = '%s'"%(k,v)
    distri_info = getDistriInfo(oracle, distri_id)
    hold_staff_id = distri_info['staff_id']
    args['hold_staff_id'] = hold_staff_id

    if(str(hold_staff_id) == str(staff_id)):
        raise Exception,'发票己经是工号%s的了,再下发没意义的,不要乱搞了'%staff_id

    is_upper_staff = upperLevel(oracle = oracle, upper_staff = oper_staff_id, lower_staff = hold_staff_id)
    if(not is_upper_staff):
        raise Exception,'工号%s没有权限操作工号%s持有的发票资源'%(oper_staff_id,hold_staff_id)

    args['hold_tax_begin_nbr'] = distri_info['tax_begin_nbr']
    args['hold_tax_end_nbr'] = distri_info['tax_end_nbr']

    tax_type = getOperType(tax_begin_nbr, tax_end_nbr,
    args['hold_tax_begin_nbr'], args['hold_tax_end_nbr'])

    args['tax_type'] = tax_type
    if(tax_type == 'a'):
        allDistri(oracle, distri_id, oper_staff_id, staff_id)
    else:
        partDistri(oracle, **args)
def allDistri(oracle, distri_id, oper_staff_id, staff_id):
    '''全部下发'''
    update_dic = {'state':'out','state_date':'/sysdate'}
    where_dic = {'distri_id':distri_id}
    update(oracle, 'distri', update_dic, where_dic)
    insertDistriLog(oracle = oracle, distri_id = distri_id, oper_staff_id = oper_staff_id, oper = 'be distri',state = 'out')
    
    new_distri_id = getNextVal(oracle)
    insertDistriAsSplit(oracle, new_distri_id = new_distri_id, distri_id = distri_id, staff_id = staff_id)
    insertDistriLog(oracle = oracle, distri_id = new_distri_id, oper_staff_id = oper_staff_id, oper = 'distri',state = 'hold')
def partDistri(oracle, **args):
    '''部分下发
    in: tax_type, distri_id, staff_id, oper_staff_id, hold_staff_id, 
                tax_begin_nbr, tax_end_nbr, 
                hold_tax_begin_nbr, hold_tax_end_nbr
    '''
    for k, v in args.items():
        log.msg("%s type is %s"%(k,type(v)))
        if (type(v) is StringType or type(v) is UnicodeType):
            exec "%s = '%s'"%(k,v)
            print "%s = '%s'"%(k,v)
        else:
            exec "%s = %s"%(k,v)
            print "%s = %s"%(k,v)
    log.msg(type(tax_end_nbr))
    checkBeginEndNbr(tax_begin_nbr, tax_end_nbr, hold_tax_begin_nbr, hold_tax_end_nbr)
    update_dic = {'state':'out','state_date':'/sysdate'}
    where_dic = {'distri_id':distri_id}
    update(oracle, 'distri', update_dic, where_dic)
    insertDistriLog(oracle, distri_id = distri_id, oper_staff_id = oper_staff_id, oper = 'part be distri',state = 'out')

    #下发
    new_distri_id = getNextVal(oracle)
    insertDistriAsSplit(oracle, new_distri_id = new_distri_id, distri_id = distri_id, staff_id = staff_id, 
                tax_begin_nbr = tax_begin_nbr, tax_end_nbr = tax_end_nbr)
    insertDistriLog(oracle = oracle, distri_id = new_distri_id, oper_staff_id = oper_staff_id, oper = 'distri', state = 'hold')

    if(tax_type == 'r'):
        '''左下发拆分'''
        #拆分生成原持有右边剩下的
        new_distri_id = getNextVal(oracle)
        split_tax_begin_nbr = addZero(len(tax_end_nbr), int(tax_end_nbr)+1)
        insertDistriAsSplit(oracle, new_distri_id = new_distri_id, distri_id = distri_id, staff_id = hold_staff_id, 
                    tax_begin_nbr = split_tax_begin_nbr , tax_end_nbr = hold_tax_end_nbr)
        insertDistriLog(oracle = oracle, distri_id = new_distri_id, oper_staff_id = oper_staff_id, oper = 'split distri',state = 'hold')
    elif(tax_type == 'l'):
        '''右下发'''
        #拆分生成原持有左边剩下的
        new_distri_id = getNextVal(oracle)
        split_tax_end_nbr = addZero(len(tax_begin_nbr), int(tax_begin_nbr)-1)
        insertDistriAsSplit(oracle, new_distri_id = new_distri_id, distri_id = distri_id, staff_id = hold_staff_id, 
                    tax_begin_nbr = hold_tax_begin_nbr , tax_end_nbr = split_tax_end_nbr)
        insertDistriLog(oracle = oracle, distri_id = new_distri_id, oper_staff_id = oper_staff_id, oper = 'split distri',state = 'hold')
    elif(tax_type == 'm'):
        '''中间下发'''
        #左边
        new_distri_id = getNextVal(oracle)
        split_tax_end_nbr = addZero(len(tax_begin_nbr), int(tax_begin_nbr)-1)
        insertDistriAsSplit(oracle, new_distri_id = new_distri_id, distri_id = distri_id, staff_id = hold_staff_id, 
                    tax_begin_nbr = hold_tax_begin_nbr , tax_end_nbr = split_tax_end_nbr)
        insertDistriLog(oracle = oracle, distri_id = new_distri_id, oper_staff_id = oper_staff_id, oper = 'split distri',state = 'hold')
        #右边
        new_distri_id = getNextVal(oracle)
        split_tax_begin_nbr = addZero(len(tax_end_nbr), int(tax_end_nbr)+1)
        insertDistriAsSplit(oracle, new_distri_id = new_distri_id, distri_id = distri_id, staff_id = hold_staff_id, 
                    tax_begin_nbr = split_tax_begin_nbr , tax_end_nbr = hold_tax_end_nbr)
        insertDistriLog(oracle = oracle, distri_id = new_distri_id, oper_staff_id = oper_staff_id, oper = 'split distri',state = 'hold')
    else:
        raise Exception,'类型错误:%s'%tax_type

def test_distriTax(oracle):
    distriTax(oracle, distri_id = 999, oper_staff_id = 22, staff_id = 776, tax_begin_nbr = '005', tax_end_nbr = '010')

if __name__ ==  "__main__":
    from oracle import Oracle
    oracle = Oracle()
    #test_getStaffId(oracle)
    test_checkIfExist(oracle)
    #test_addDistri(oracle)
    oracle.commit()
