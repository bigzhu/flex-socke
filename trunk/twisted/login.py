#!/usr/bin/env python
#encoding=utf-8
import hashlib
from select_ import select
from update_ import update
from insert_ import insert
from insert_ import insertLog
from exp import Warning_


def login(oracle, **args):
    '''登录工号 staff_id, passwd'''
    for k, v in args.items():
        exec "%s = '%s'"%(k,v)

    select_colums = ['passwd', 'staff_desc', 'staff_id', 'state']
    sql = 'from staff where staff_id = %s'%staff_id
    result = select(oracle, select_colums, sql)
    if(result == None):
        raise Warning_,'工号%s不存在'%staff_id
    staff_info = result[0]
    #工号是否有效
    if(staff_info['state'] == '0'):
        raise Warning_,'这个工号已经被管理员删除了,有疑问请联系管理员!'


    #加密
    m = hashlib.md5()
    m.update(passwd)
    in_passwd = m.hexdigest()
    if(staff_info['passwd'] ==  None):
        raise Warning_,'这个工号竟然没设密码!'

    if(staff_info['passwd'].upper()!=  in_passwd.upper()):
        raise Warning_,'密码错误!'


    select_colums = ['r.name role_name', 'r.role_id']
    sql =  '''from staff_role sr,role r
            where  sr.staff_id = %s
            and sr.role_id = r.role_id
            '''%staff_id
    result = select(oracle, select_colums, sql)
    if(result == None):
        #raise Warning_,'工号%s没有角色或者机构'%staff_id
        result = [staff_info]
    else:
        result[0].update(staff_info)

    select_colums = ['b.name bss_org_name', 'b.bss_org_id']
    sql =  '''
            from staff s, bss_org b
             where s.bss_org_id = b.bss_org_id
               and s.staff_id = %s
         '''%staff_id
    bss_info = select(oracle, select_colums, sql)
    if(bss_info == None):
        raise Warning_,'工号%s没有机构'%staff_id
    else:
        result[0].update(bss_info[0])

    return result
def test_loginStaff(oracle):
    print login(oracle, staff_id = '22', passwd = 'bigzhu')
if __name__ ==  "__main__":
    from oracle import Oracle
    oracle = Oracle()
    test_loginStaff(oracle)
    oracle.commit()
