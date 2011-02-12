# -*- coding:UTF-8 -*-
''' 发票作废 '''
from oracle import Oracle
from pool import selectPool
from pool import updatePool
from select_ import select
from update_ import update
from datetime import datetime
from insert_ import insertLog

def nullifyTax(oracle, dic):
    ''' 发票作废
        tax_code
        tax_nbr
        oper_staff_id
        remark
    '''
    pool_id = getPoolId(oracle, dic)
    updateToNullify(oracle, pool_id)
    addPoolLog(oracle, dic, pool_id)

def getPoolId(oracle, dic):
    '''取得已经上架的发票pool_id'''
    select_colums = ['pool_id']
    where_dic = {}
    where_dic['tax_code'] = dic['tax_code']
    where_dic['tax_nbr'] = dic['tax_nbr']
    #where_dic['state'] = 'instance'
    sql = 'from pool'
    and_the = "and state in('instance','pre-use')"
    select_value = select(oracle, select_colums, sql, where_dic, and_the)
    #select_value = selectPool(oracle, select_colums, where_dic, and_the)
    if(select_value ==  None):
        raise Exception, '上架/预打记录数有%s条,tax_code = %s,tax_nbr = %s'%(0, where_dic['tax_code'], where_dic['tax_nbr'])
    if(len(select_value)!= 1):
        raise Exception, '上架/预打记录数有%s条,tax_code = %s,tax_nbr = %s'%(len(select_value), where_dic['tax_code'], where_dic['tax_nbr'])
    pool_id = select_value[0]['pool_id']
    return pool_id
def testGetPoolId():
    oracle = Oracle()
    dic = {'tax_code':'123', 'tax_nbr':'456'}
    print getPoolId(oracle, dic)
def updateToNullify(oracle, pool_id):
    '''更新instance为nullify'''
    update_dic = {'state':'nullify', 'state_date':'/sysdate'}
    where_dic = {'pool_id':pool_id}

    #row_count = updatePool(oracle, update_dic, where_dic)
    #if(row_count!= 1):
    #    raise Exception, '作废录数有%s条,pool_id = %s'%(row_count, pool_id)
    and_the = "and state in('instance', 'pre-use')"

    update(oracle = oracle, table_name = 'pool', update_dic = update_dic,
    where_dic = where_dic, and_the = and_the)
def addPoolLog(oracle, dic, pool_id):
    where_dic = {}
    where_dic['pool_id'] = pool_id
    add_infos = {'oper':'nullify'}
    add_infos['oper_staff_id'] = dic['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'pool', where_dic, add_infos)

def test_nullifyTax():
    oracle = Oracle()
    dic = {'tax_code':'123456789012','tax_nbr':'000000100', 'oper_staff_id':13, 'remark':'作废'}
    print nullifyTax(oracle, dic)
    oracle.commit()   
def test_getPoolId():
    oracle = Oracle()
    select_colums = ['pool_id', 'tax_code', 'tax_nbr']
    where_dic = {'tax_code':'1234567','tax_nbr':'100204'}
    print selectPool(oracle, select_colums, where_dic)

if __name__ ==  "__main__":
    test_nullifyTax()
    #testGetPoolId()
    #test_getPoolId()
