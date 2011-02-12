# -*- coding:UTF-8 -*-
''' 入库发票作废 '''
from oracle import Oracle
from update_ import update
from datetime import datetime
from insert_ import insertLog

def nullifyDistri(oracle, **args):
    ''' 入库发票作废
        distri_id
        oper_staff_id
        remark
    '''
    for k, v in args.items():
        exec "%s = '%s'"%(k,v)
    updateToNullify(oracle, distri_id, oper_staff_id )
    addDistriLog(oracle, distri_id, oper_staff_id)
def updateToNullify(oracle, distri_id, oper_staff_id):
    '''更新in为nullify'''
    update_dic = {'state':'nullify','state_date':'/sysdate'}
    where_dic = {'distri_id':distri_id, 'staff_id':oper_staff_id}
    and_the = "and state in('in','hold')"

    update(oracle, 'distri', update_dic, where_dic, and_the = and_the)
def addDistriLog(oracle, distri_id, oper_staff_id):
    where_dic = {}
    where_dic['distri_id'] = distri_id
    add_infos = {'oper':'nullify'}
    add_infos['oper_staff_id'] = oper_staff_id
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'distri', where_dic, add_infos)

def test_nullifyDistri():
    oracle = Oracle()
    dic = {'distri_id':'1105', 'oper_staff_id':71, 'remark':'作废'}
    print nullifyDistri(oracle, **dic)
    oracle.commit()   

if __name__ ==  "__main__":
    test_nullifyDistri()

    #test_getPoolId()
