# -*- coding:UTF-8 -*-
from oracle import Oracle
import xml.etree.ElementTree as ElementTree
from select_ import select
from insert_ import insert
from insert_ import insertLog
from update_ import update
from exp import Warning_
def getBssOrgID(oracle):
    '''给出最小的一个还未用的bss_org_id'''
    select_colums = ['bss_org_id']
    sql = ''' from (SELECT min(bss_org_id), max(bss_org_id)+1 bss_org_id
          FROM (SELECT bss_org_id,
                       TO_NUMBER(bss_org_id) -
                       (ROW_NUMBER() OVER(ORDER BY bss_org_id)) DIF
                  FROM bss_org)
         GROUP BY DIF)
 where rownum < 2'''
    return select(oracle, select_colums, sql)
def testGetBssOrgID(oracle):
    print getBssOrgID(oracle)

def getBssOrgStaff(oracle, bss_org_id):
    ''' 从数据库中获取机构和工号树信息 '''
    bss_org_dic = {}
    sql = '''
             select bss_org_id,null, name, bss_parent_org_id
               from bss_org
             connect by prior bss_org_id = bss_parent_org_id
              start with bss_org_id   = :bss_org_id
             union all
             select null,staff_id, staff_desc, bss_org_id
               from staff s
              where s.BSS_ORG_ID in
                    (select bss_org_id
                       from bss_org
                     connect by prior bss_org_id = bss_parent_org_id
                      start with bss_org_id  = :bss_org_id)
                    and s.state = '1'
            '''
    dic = {'bss_org_id':bss_org_id}
    select_result = oracle.execute(sql, dic)
    #建立根节点
    root = ElementTree.Element('root')
    #tree = ElementTree.ElementTree(root)
    bss_org_dic["root"] = root
    for bss_org in select_result:
        bss_org_id = bss_org[0]
        staff_id = bss_org[1]
        name = bss_org[2]
        bss_parent_org_id = bss_org[3]
        if(bss_parent_org_id ==  None):
            parent_element = root
        else:
            parent_element = bss_org_dic.get(bss_parent_org_id)
            if(parent_element ==  None):
                parent_element = root
        element = ElementTree.SubElement(parent_element, 'n')
        bss_org_dic[bss_org_id] = element
        if(bss_org_id !=  None):
            element.set("bss_org_id", str(bss_org_id))
        element.set("name", name)
        if(staff_id !=  None):
            element.set("staff_id", str(staff_id))
    return root.getchildren()[0]
def testGetBssOrgStaff(oracle):
    element = getBssOrgStaff(oracle, '1')
    print ElementTree.tostring(element)

class BssOrg:
    def __init__(self, oracle, **args):
        self.oracle = oracle
        self.oper_staff_id = args['oper_staff_id']
        self.bss_org_id = args['bss_org_id']
        self.args = args
        del args['oper_staff_id']
    def addBssOrg(self):
        insert(self.oracle, 'bss_org', self.args)

        add_infos = {'oper':'add', 'oper_staff_id':self.oper_staff_id,
        'oper_date':'/sysdate'}
        insertLog(self.oracle, 'bss_org', {'bss_org_id':self.bss_org_id},
        add_infos)
    def delBssOrg(self):
        if(hasChrild(self.oracle, self.bss_org_id) is not None):
            raise Warning_,'请先删除子机构'
        if(hasStaff(self.oracle, self.bss_org_id) is not None):
            raise Warning_,'机构%s下还有工号,请先删除该机构下的工号' % self.bss_org_id
    
        add_infos = {'oper':'del', 'oper_staff_id':self.oper_staff_id,
        'oper_date':'/sysdate'}
        insertLog(self.oracle, 'bss_org', {'bss_org_id':self.bss_org_id},
        add_infos)
    
        sql = 'delete from bss_org where bss_org_id = %s' % self.bss_org_id
        row_count = self.oracle.execute(sql)
        if(row_count!= 1):
            raise Exception,'删除机构%s %s个,出现异常' % (self.bss_org_id, row_count)
    def changeBssOrg(self):
        update_dic = self.args
        del update_dic['bss_org_id']
        update(self.oracle, 'bss_org', update_dic, where_dic =
        {'bss_org_id':self.bss_org_id})

        add_infos = {'oper':'change', 'oper_staff_id':self.oper_staff_id,
        'oper_date':'/sysdate'}
        insertLog(self.oracle, 'bss_org', {'bss_org_id':self.bss_org_id},
        add_infos)

def addBssOrg(oracle, **args):
    '''depend on flex'''
    bss_org = BssOrg(oracle, **args)
    bss_org.addBssOrg()
def testAddBssOrg(oracle):
    dic = {'bss_org_id':666, 'oper_staff_id':78, 'name':'bigzhu'}
    addBssOrg(oracle, **dic)

def delBssOrg(oracle, **args):
    bss_org = BssOrg(oracle, **args)
    bss_org.delBssOrg()
def testDelBssOrg(oracle):
    dic = {'bss_org_id':87354}
    delBssOrg(oracle, **dic)

def changeBssOrg(oracle, **args):
    bss_org = BssOrg(oracle, **args)
    bss_org.changeBssOrg()
def testChangeBssOrg(oracle):
    dic = {'bss_org_id':2, 'name':'联创', 'oper_staff_id':71}
    changeBssOrg(oracle, **dic)


def hasChrild(oracle, bss_org_id):
    return select(oracle, ['bss_org_id'], 'from bss_org', where_dic =
    {'bss_parent_org_id':bss_org_id})
def hasStaff(oracle, bss_org_id):
    return select(oracle, ['staff_id'], 'from staff', where_dic =
    {'bss_org_id':bss_org_id})

def testHasChrild(oracle):
    hasChrild(oracle, '1')
   
if __name__ ==  "__main__":
    oracle_test = Oracle()
    #element = getBssOrgStaff(oracle, '373')
    testGetBssOrgStaff(oracle_test)
    #print testHasChrild(oracle)
    #print testAddBssOrg(oracle)
    #print testDelBssOrg(oracle)
    #testChangeBssOrg(oracle)
    #test_getBssOrgID(oracle)
    #test_getBssOrgRetail(oracle)
    oracle_test.commit()
