# -*- coding:UTF-8 -*-
from select_ import select
from update_ import update
from insert_ import insert
from insert_ import insertLog
from exp import Warning_
from delete import delete
def addRole(oracle, **args):
    '''增加角色 dic: role_id'''
    select_colums = ['role_id','name']
    where_dic = {}
    where_dic['role_id'] = args['role_id']
    sql = 'from role'
    role_info = select(oracle, select_colums, sql, where_dic)
    if(role_info!= None):
        raise Exception, '角色%s(%s)已经存在'%(role_info[0]['role_id'], role_info[0]['name'] )

    insert_value = args.copy()
    del insert_value['oper_staff_id']
    insert_value['state_date'] = '/sysdate'
    insert(oracle, 'role', insert_value)

    where_dic = {}
    where_dic['role_id'] = args['role_id']
    add_infos = {'oper':'add'}
    add_infos['oper_staff_id'] = args['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'role', where_dic, add_infos)
def delRole(oracle, **args):
    '''删除角色 role_id oper_staff_id'''
    where_dic = {}
    where_dic['role_id'] = args['role_id']

    #是否有工号是这个角色的
    select_colums = ['staff_id']
    sql = 'from staff_role'
    staff_role_info = select(oracle, select_colums, sql, where_dic)
    if(staff_role_info!= None):
        raise Warning_, '角色role_id = %s下还有工号,请先删除工号角色关系后再删除该工号'%(args['role_id'])


    add_infos = {'oper':'del'}
    add_infos['oper_staff_id'] = args['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'role', where_dic, add_infos)

    sql = 'delete from role where role_id = %s'%args['role_id']
    row_count = oracle.execute(sql)
    if(row_count ==  0):
        raise Exception, '未能正确删除role表;role_id = %s'%args['role_id']

def addRolePrivilege(oracle, **args):
    select_colums = ['role_id']
    where_dic = {}
    where_dic['role_id'] = args['role_id']
    sql = 'from role'
    role_info = select(oracle, select_colums, sql, where_dic)
    if(role_info == None):
        raise Warning_, '角色role_id = %s不存在'%(args['role_id'])


    select_colums = ['role_id','privilege_id']
    where_dic = {}
    where_dic['role_id'] = args['role_id']
    where_dic['privilege_id'] = args['privilege_id']
    sql = 'from role_privilege'
    role_info = select(oracle, select_colums, sql, where_dic)
    if(role_info!= None):
        raise Warning_, '角色权限role_id = %s privilege_id = %s已经存在'%(role_info[0]['role_id'], role_info[0]['privilege_id'] )

    insert_value = args.copy()
    del insert_value['oper_staff_id']
    insert(oracle, 'role_privilege', insert_value)

    where_dic = {}
    where_dic['role_id'] = args['role_id']
    where_dic['privilege_id'] = args['privilege_id']
    add_infos = {'oper':'add'}
    add_infos['oper_staff_id'] = args['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'role_privilege', where_dic, add_infos)
def delRolePrivilege(oracle, **args):
    '''删除角色权限 role_id oper_staff_id privilege_id'''
    for k, v in args.items():
        exec "%s = '%s'"%(k,v)
    where_dic = {}
    where_dic['role_id'] = role_id
    where_dic['privilege_id'] = privilege_id
    add_infos = {'oper':'del'}
    add_infos['oper_staff_id'] = args['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'role_privilege', where_dic, add_infos)

    where_dic = {'role_id':role_id, 'privilege_id':privilege_id}
    delete(oracle = oracle, table_name = 'role_privilege', where_dic = where_dic)

def modifyRole(oracle, **args):
    '''role_id, oper_staff_id '''
    update_dic = args
    role_id = update_dic['role_id']
    oper_staff_id = update_dic['oper_staff_id']
    del update_dic['role_id']
    del update_dic['oper_staff_id']
    update(oracle, 'role', update_dic, where_dic = {'role_id':role_id})

    add_infos = {'oper':'modify', 'oper_staff_id':oper_staff_id, 'oper_date':'/sysdate'}
    insertLog(oracle, 'role', {'role_id':role_id}, add_infos)


def test_addRole(oracle):
    dic = {}
    dic['role_id'] = '198474'
    dic['role_desc'] = 'bigzhu'
    dic['name'] = 'bigzhu'
    dic['oper_staff_id'] = 22
    addRole(oracle, **dic)
def test_addRolePrivilege(oracle):
    dic = {}
    dic['role_id'] = '1'
    dic['privilege_id'] = 'id_nav_crm_bss_org_retail'
    dic['oper_staff_id'] = 1
    addRolePrivilege(oracle, **dic)
def test_delRole():
    dic = {}
    dic['role_id'] = '198474'
    dic['oper_staff_id'] = 22
    delRole(oracle, **dic)
def test_delRolePrivilege():
    dic = {}
    dic['role_id'] = '198474'
    dic['privilege_id'] = 1
    dic['oper_staff_id'] = 22
    delRolePrivilege(oracle, **dic)

   
if __name__ ==  "__main__":
    from oracle import Oracle
    oracle = Oracle()
    #test_addRole(oracle)
    test_addRolePrivilege(oracle)
    #test_delRole()
    #test_delRolePrivilege()
    oracle.commit()
