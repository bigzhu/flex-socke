# -*- coding:UTF-8 -*-
import xml.etree.ElementTree as ElementTree
def getPrivilege(oracle, staff_id):
    '''从数据库中获取所有权限信息'''
    privilege_dic = {}
    dic = {'privilege_id':'1', 'staff_id':staff_id}
    sql = '''
                select 
                p.privilege_id,
                p.parent_privilegeid,
                p.order_id,
                p.privilege_name,
                p.privilege_desc
            from privilege p                                 
        where                               
            p.privilege_id in													
            (                                                           
             select privilege_id from role_privilege where role_id in (select role_id from staff_role where staff_id = :staff_id))
            and p.privilege_id<>:privilege_id
        connect by prior p.privilege_id = p.parent_privilegeid
         start with p.privilege_id = :privilege_id
            '''
    select_result = oracle.execute(sql, dic)
    #建立根节点
    root = ElementTree.Element('root')
    root.set("privilege_name", '菜单')
    tree = ElementTree.ElementTree(root)
    privilege_dic["root"] = root
    for privilege in select_result:
        privilege_id = str(privilege[0])
        parent_privilege_id = str(privilege[1])
        if(parent_privilege_id ==  None):
            parent_element = root
        if(parent_privilege_id ==  '1'):
            parent_element = root
        else:
            parent_element = privilege_dic.get(parent_privilege_id)
            if(parent_element ==  None):
                parent_element = root
        element = ElementTree.SubElement(parent_element,"node")
        privilege_dic[privilege_id] = element
        element.set("privilege_id", privilege_id)
        element.set("parent_privilege_id", parent_privilege_id)
        element.set("order_id", str(privilege[2]))
        element.set("privilege_name", str(privilege[3]))
        element.set("privilege_desc", str(privilege[4]))
    return root

def addPrivilege(oracle, **agrs):
    pass

def test_getPrivilege():
    from oracle import Oracle
    oracle = Oracle()

    element = getPrivilege(oracle, 22)
    print ElementTree.tostring(element)

if __name__ ==  "__main__":
    test_getPrivilege()
