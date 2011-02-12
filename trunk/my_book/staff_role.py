# -*- coding:UTF-8 -*-
from select_ import select
from update_ import update
from insert_ import insert
from insert_ import insertLog
from exp import Warning_
from delete import delete

def addStaffRole(oracle, **args):
    '''增加工号角色 dic: role_id, staff_id, oper_staff_id'''
    insert_value = args.copy()
    del insert_value['oper_staff_id']
    where_dic = insert_value

    select_colums = ['role_id','staff_id']
    sql = 'from staff_role'
    role_info = select(oracle, select_colums, sql, where_dic)
    print role_info
    if(role_info!= None):
        raise Warning_, '角色%s己经挂到工号%s上了'%(role_info[0]['role_id'], role_info[0]['staff_id'] )

    insert(oracle, 'staff_role', insert_value)

    add_infos = {'oper':'add'}
    add_infos['oper_staff_id'] = args['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'staff_role', where_dic, add_infos)
def delStaffRole(oracle, **args):
    '''删除工号角色 dic: role_id, staff_id, oper_staff_id'''
    insert_value = args.copy()
    del insert_value['oper_staff_id']
    where_dic = insert_value

    select_colums = ['role_id','staff_id']
    sql = 'from staff_role'
    role_info = select(oracle, select_colums, sql, where_dic)
    print role_info
    if(role_info == None):
        raise Warning_, '角色%s工号%s己经不存在,无需删除'%(role_info[0]['role_id'], role_info[0]['staff_id'] )

    add_infos = {'oper':'del'}
    add_infos['oper_staff_id'] = args['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'staff_role', where_dic, add_infos)

    delete(oracle = oracle, table_name = 'staff_role', where_dic = where_dic)
def test_delStaffRole(oracle):
    dic = {}
    dic['role_id'] = '6'
    dic['staff_id'] = '71'
    dic['oper_staff_id'] = '22'
    delStaffRole(oracle, **dic)

def test_addStaffRole(oracle):
    dic = {}
    dic['role_id'] = '6'
    dic['staff_id'] = '71'
    dic['oper_staff_id'] = '22'
    addStaffRole(oracle, **dic)
   
if __name__ ==  "__main__":
    from oracle import Oracle
    oracle = Oracle()
    #test_addStaffRole(oracle)
    test_delStaffRole(oracle)
    oracle.commit()
