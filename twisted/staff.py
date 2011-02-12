# -*- coding:UTF-8 -*-
import hashlib
from select_ import select
from update_ import update
from insert_ import insert
from insert_ import insertLog
from exp import Warning_

def upperLevel(oracle,upper_staff,lower_staff):
    ''' 判断工号是否为上下级'''
    sql = '''
        select *
          from staff
         where staff_id = %s
           and bss_org_id in
               (select bss_org_id
                  from bss_org
                connect by bss_org_id = prior bss_parent_org_id
                 start with bss_org_id = (select max(bss_org_id)
                                            from staff
                                           where staff_id = %s))
    '''%(upper_staff,lower_staff)
    select_result = oracle.execute(sql)
    if(len(select_result) !=  0):
        return True
    else:
        return False
def getStaff(oracle, staff_id):
    '''查询工号'''
    select_colums = ['staff_id', 'staff_desc', 'bss_org_id']
    sql = 'from staff '
    where_dic = {'staff_id':staff_id}
    return select(oracle, select_colums, sql, where_dic)
def addStaff(oracle, dic):
    '''增加工号 dic: staff_id, staff_desc, passwd, bss_org_id, oper_staff_id, [remark]'''
    dic['staff_id'] = int(dic['staff_id'])
    dic['bss_org_id'] = int(dic['bss_org_id'])
    dic['oper_staff_id'] = int(dic['oper_staff_id'])
    dic['state'] = '1'
    staff_info = getStaff(oracle, dic['staff_id'])
    if(staff_info!= None):
        staff_info = staff_info[0]
        print staff_info
        raise Exception, '工号%s(%s)已经存在,属于机构 %s'%(staff_info['staff_id'], staff_info['staff_desc'], staff_info['bss_org_id'])

    #加密
    passwd = dic['passwd']
    m = hashlib.md5()
    m.update(passwd)
    dic['passwd'] = m.hexdigest()

    dic2 = dic.copy()
    print dic2
    del dic2['oper_staff_id']
    if(dic2.get('remark')):
        del dic2['remark']
    row_count = insert(oracle, 'staff', dic2)

    where_dic = {}
    where_dic['staff_id'] = dic['staff_id']
    add_infos = {'oper':'add staff'}
    add_infos['oper_staff_id'] = dic['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'staff', where_dic, add_infos)
def delStaff(oracle, **args):
    '''删除工号 staff_id, oper_staff_id, [remark]'''
    for k, v in args.items():
        exec "%s = '%s'"%(k,v)
    is_upper = upperLevel(oracle, oper_staff_id, staff_id)
    if(not is_upper):
        raise Exception,'工号%s没有权限删除工号%s'%(oper_staff_id, staff_id)
    #sql = 'delete from staff where staff_id = %s'%staff_id
    update(oracle, 'staff', update_dic = {'state':'0'}, where_dic = {'staff_id':staff_id})
    #row_count = oracle.execute(sql)
    #if(row_count ==  0):
    #    raise Exception, '未能正确删除staff表;staff_id = %s'%staff_id

    add_infos = {'oper':'del', 'oper_staff_id':oper_staff_id, 'oper_date':'/sysdate'}
    insertLog(oracle, 'staff', {'staff_id':staff_id}, add_infos)


def test_delStaff(oracle):
    dic = {'staff_id':71, 'oper_staff_id':22}
    delStaff(oracle, **dic)
def changeStaff(oracle, **args):
    '''staff_id, oper_staff_id '''
    update_dic = args
    passwd = update_dic.get('passwd')
    if( passwd!= None):
        m = hashlib.md5()
        m.update(passwd)
        passwd = m.hexdigest()
        update_dic['passwd'] = passwd
    staff_id = update_dic['staff_id']
    oper_staff_id = update_dic['oper_staff_id']
    del update_dic['staff_id']
    del update_dic['oper_staff_id']
    update(oracle, 'staff', update_dic, where_dic = {'staff_id':staff_id})

    add_infos = {'oper':'modify', 'oper_staff_id':oper_staff_id, 'oper_date':'/sysdate'}
    insertLog(oracle, 'staff', {'staff_id':staff_id}, add_infos)
def loginStaff(oracle, **args):
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

def bondStaff(oracle, **args):
    '''工号绑定 staff_id out_staff_id sys_type passwd sys_type'''
    for k, v in args.items():
        exec "%s = '%s'"%(k,v)
    if(sys_type!= 'C' and sys_type!= 'B'):
        raise Warning_,'绑定工号时传入的系统类型为%s,不正确'

    result = select(oracle, ['out_staff_id','sys_type'], 'from staff_map', {'staff_id':staff_id, 'state':'1','sys_type':sys_type})
    if(result!= None):
        raise Warning_,'工号%s已经绑定到系统%s的工号%s,不能重复绑定'%(staff_id, result[0]['sys_type'], result[0]['out_staff_id'])

    result = select(oracle, ['staff_id'], 'from staff_map', {'out_staff_id':out_staff_id, 'state':'1', 'sys_type':sys_type})
    if(result!= None):
        raise Exception,'系统%s工号%s已经绑定到了工号%s上,不能重复绑定'%(sys_type, out_staff_id, result[0]['staff_id'])


    if(sys_type == 'C'):
        result = oracle.execute('select passwd,staff_id from v_staff_crm where upper(staff_id) = :staff_id',{'staff_id':out_staff_id.upper()})
    elif(sys_type == 'B'):
        result = oracle.execute('select passwd,staff_id from acct.staff where upper(staff_code) = :staff_id',{'staff_id':out_staff_id.upper()})

    if(len(result) == 0):
        raise Warning_,'外部系统%s 工号%s不存在'%(sys_type,out_staff_id)
    crm_passwd = result[0][0]
    out_staff_id = result[0][1]


    if(sys_type == 'C'):
        m = hashlib.md5()
        m.update(passwd)
        passwd = m.hexdigest().upper()

        if(passwd!= crm_passwd):
            raise Warning_,'crm工号%s在密码不正确'%out_staff_id


    insert_dic = {'staff_id':staff_id, 'out_staff_id':out_staff_id, 'state':1, 'sys_type':sys_type, 'created_date':'/sysdate', 'state_date':'/sysdate'}
    insert(oracle, 'staff_map', insert_dic)
def unbondStaff(oracle, **args):
    '''工号取消绑定 staff_id out_staff_id sys_type '''
    for k, v in args.items():
        exec "%s = '%s'"%(k,v)
    update_dic = {'state':'0'}
    where_dic = args
    update(oracle, 'staff_map', update_dic, where_dic)

def getStaffID(oracle):
    '''给出最小的一个还未用的staff_id'''
    select_colums = ['staff_id']
    sql = ''' from (SELECT min(staff_id), max(staff_id)+1 staff_id
          FROM (SELECT staff_id,
                       TO_NUMBER(staff_id) -
                       (ROW_NUMBER() OVER(ORDER BY staff_id)) DIF
                  FROM staff)
         GROUP BY DIF)
 where rownum < 2'''
    return select(oracle, select_colums, sql)
def test_getStaffID(oracle):
    print getStaffID(oracle)

def getRealStaffID(oracle, staff_id, sys_type):
    ''' 从绑定表中取电子发票的 staff_id '''
    where_dic = {'out_staff_id':staff_id, 'sys_type':sys_type, 'state':'1'}
    result = select(oracle, ['staff_id'], 'from staff_map', where_dic)
    if(result == None):
        raise Warning_,'工号 %s 不存在绑定关系'%staff_id
    else:
        return result[0]['staff_id']

def test_getRealStaffID(oracle):
    print getRealStaffID(oracle, 'SMLJ', 'C')


def test_loginStaff(oracle):
    print loginStaff(oracle, staff_id = '22', passwd = 'a123456')
def test_changeStaff(oracle):
    dic = {'staff_id':22, 'staff_desc':'大乔', 'oper_staff_id':71}
    changeStaff(oracle, **dic)
def test_boundStaff(oracle):
    dic = {'staff_id':71, 'out_staff_id':710018, 'sys_type':'C', 'oper_staff_id':1, 'passwd':'wl78912'}
    bondStaff(oracle, **dic)
def test_unboundStaff(oracle):
    dic = {'staff_id':71, 'out_staff_id':1001, 'sys_type':'C'}
    unbondStaff(oracle, **dic)

if __name__ ==  "__main__":
    from oracle import Oracle
    oracle = Oracle()

    result = getStaff(oracle, 22)
    #print result
    print result[0]['staff_desc']
    print result[1]['staff_desc']
    #print result['staff_id']
    #for i in getStaff(oracle, 22)[0]:
    #    print getStaff(oracle, 22)[0][i]
    #test_getRealStaffID(oracle)
    #dic = {'id1':{'id1':12}, 'id2':56, 'id3':67}
    #print dic
    #test_getStaffID(oracle)
    #test_loginStaff(oracle)
    #test_changeStaff(oracle)
    #test_boundStaff(oracle)
    #test_delStaff(oracle)
    #test_unboundStaff(oracle)
    oracle.commit()
