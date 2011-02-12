# -*- coding:UTF-8 -*-
from oracle import Oracle
import xml.etree.ElementTree as ElementTree
from twisted.internet import defer
from select_ import select
from insert_ import insert
from insert_ import insertLog
from datetime import datetime
from update_ import update
from exp import Warning_

def getOrg(oracle, dic):
    ''' 从数据库中获取机构和点信息 '''
    for k, v in dic.items():
        exec "%s = '%s'"%(k,v)
    org_dic = {}
    sql = '''
            select id, name, parent_id, type
              from org
            connect by prior id = parent_id
             start with id in
                        (select parent_id
                           from org
                          where id  = %s)'''%id
    select_result = oracle.execute(sql)
    #建立根节点
    root = ElementTree.Element('root')
    tree = ElementTree.ElementTree(root)
    org_dic["root"] = root
    'id, name, parent_id, type'
    for bss_org in select_result:
        id = bss_org[0]
        name = bss_org[1]
        parent_id = bss_org[2]
        type = bss_org[3]
        if(parent_id ==  None):
            parent_element = root
        else:
            parent_element = org_dic.get(parent_id)
            if(parent_element ==  None):
                parent_element = root
        element = ElementTree.SubElement(parent_element, 'n')
        org_dic[id] = element
        if(id !=  None):
            element.set("id", str(id))
            element.set("parent_id", str(parent_id))
        element.set("name", name)
        element.set("type", type)
    return root.getchildren()[0]
def test_getOrg(oracle):
    element = getOrg(oracle, {'id':2})
    print ElementTree.tostring(element)
def getOrgID(oracle):
    '''给出最小的一个还未用的org_id'''
    select_colums = ['id']
    sql = ''' from (SELECT min(id), max(id)+1 id
          FROM (SELECT id,
                       TO_NUMBER(id) -
                       (ROW_NUMBER() OVER(ORDER BY id)) DIF
                  FROM org)
         GROUP BY DIF)
            where rownum < 2'''
    return select(oracle, select_colums, sql)
def test_getOrgID(oracle):
    print getOrgID(oracle)

def addOrg(oracle, dic):
    '''depend on flex'''
    for k, v in dic.items():
        exec "%s = '%s'"%(k,v)
    print dic.__doc__
    if('id' in dic):
        id = dic['id']
    else:
        select_result = select(oracle, ['org_seq.nextval'], 'from dual')
        id = select_result[0]['nextval']
        dic['id'] = id;

    del dic['oper_staff_id']
    insert(oracle, 'org', dic)

    add_infos = {'oper':'add', 'oper_staff_id':oper_staff_id, 'oper_date':'/sysdate'}
    insertLog(oracle, 'org', {'id':id}, add_infos)
def test_addOrg(oracle):
    dic = {'id':'5','name':'bigzhu', 'type':'org', 'parent_id':4, 'oper_staff_id':1}
    element = addOrg(oracle, dic)

def hasChrild(oracle, id):
    return select(oracle, ['id'], 'from org',where_dic = {'parent_id':id})

def delOrg(oracle, args):
    '''id, oper_staff_id'''
    for k, v in args.items():
        exec "%s = '%s'"%(k,v)
    if(hasChrild(oracle, id)!= None):
        raise Warning_,'请先删除机构下的其他信息'

    add_infos = {'oper':'del', 'oper_staff_id':oper_staff_id, 'oper_date':'/sysdate'}
    insertLog(oracle, 'org', {'id':id}, add_infos)

    sql = 'delete from org where id = %s'%id
    row_count = oracle.execute(sql)
    if(row_count!= 1):
        raise Exception,'删除机构%s %s个,出现异常'%(id, row_count)
def test_delBssOrg(oracle):
    dic = {'bss_org_id':87354}
    delBssOrg(oracle,**dic)

def changeRetail(oracle, dic):
    ''' id, flex_id, name, score, value, num'''
    for k, v in dic.items():
        exec "%s = '%s'"%(k,v)
    where_dic = {'id':id, 'flex_id':flex_id}
    update_dic = {'num':num, 'name':name, 'score':score, 'value':value, 'state_date':'/sysdate'}
    count = update(oracle = oracle, table_name = 'retail_detail', update_dic = update_dic, where_dic = where_dic, count = 0)
    if(count == 0):
        dic['state_date'] = '/sysdate'
        insert(oracle, 'retail_detail', dic)

    #add_infos = {'oper':'add', 'oper_staff_id':oper_staff_id, 'oper_date':'/sysdate'}
    #insertLog(oracle, 'org', {'id':id}, add_infos)
def getRetailInfo(oracle, dic):
    ''' retail_id '''
    for k, v in dic.items():
        exec "%s = '%s'"%(k,v)

    return select(oracle, ['flex_id', 'name', 'score', 'value','num' ], 'from retail_detail', {'id':retail_id})

def test_getRetailInfo(oracle):
    dic = {'retail_id':1111}
    getRetailInfo(oracle, dic)

if __name__ ==  "__main__":
    oracle = Oracle()
    #test_getOrg(oracle)
    #test_addOrg(oracle)
    test_getRetailInfo(oracle)
    #test_getOrgID(oracle)
    oracle.commit()
