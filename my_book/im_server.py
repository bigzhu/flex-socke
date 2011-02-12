# -*- coding:UTF-8 -*-
from twisted.internet import defer

from hello import hello
from get_tax import *

from staff import *
from retail import *

from hand import handPrint
from staff_role import addStaffRole
from staff_role import  delStaffRole
from oracle import Oracle
from call_back import right,error
from exp import *
from roll_tax import roll
from select_ import select
from collect_tax import collectTax
from nullify_tax import nullifyTax
from pool import addNote
from bbs import *
from privilege import getPrivilege
from bss_org import *
from role import *
from distri import *
from distri import distriTax
from instance_tax import instanceTax
from nullify_distri import nullifyDistri
from adjust import adjustError
from abstract_tax import abstractTax

class Server():
    def __init__(self):
        oracle = Oracle()

    def handPrint(self, args):
        ''' 手工发票 '''
        try:
            oracle = Oracle()
            return defer.succeed(handPrint(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def getTax(self, staff_id):
        ''' 取发票 '''
        try:
            oracle = Oracle()
            return defer.succeed(getTax(oracle, staff_id))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def hello(self, who):
        ''' test '''
        try:
            oracle = Oracle()
            return defer.succeed(hello(who))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())
    def selectBbs(self, args):
        ''' 查询聊天室 '''
        try:
            oracle = Oracle()
            return defer.succeed(selectBbs(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())
    def modifyRole(self, args):
        ''' 修改角色 '''
        try:
            oracle = Oracle()
            return defer.succeed(modifyRole(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def checkIfExist(self, args):
        '''检查号段是否重叠'''
        try:
            oracle = Oracle()
            return defer.succeed(checkIfExist(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())


    def getBssOrgID(self):
        '''给出最小的一个还未用的bss_org_id'''
        try:
            oracle = Oracle()
            return defer.succeed(getBssOrgID(oracle))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())


    def getStaffID(self):
        '''给出最小的一个还未用的staff_id'''
        try:
            oracle = Oracle()
            return defer.succeed(getStaffID(oracle))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())


    def delStaffRole(self, args):
        '''删除工号角色 args: role_id, staff_id, oper_staff_id'''
        try:
            oracle = Oracle()
            return defer.succeed(delStaffRole(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())


    def addStaffRole(self, args):
        '''增加工号角色 args: role_id, staff_id, oper_staff_id'''
        try:
            oracle = Oracle()
            return defer.succeed(addStaffRole(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())


    def changeStaff(self, args):
        '''depend on flex'''
        try:
            oracle = Oracle()
            return defer.succeed(changeStaff(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def changeBssOrg(self, args):
        '''depend on flex'''
        try:
            oracle = Oracle()
            return defer.succeed(changeBssOrg(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def delBssOrg(self, args):
        '''depend on flex'''
        try:
            oracle = Oracle()
            return defer.succeed(delBssOrg(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def addBssOrg(self, args):
        '''depend on flex'''
        try:
            oracle = Oracle()
            return defer.succeed(addBssOrg(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def unbondStaff(self, args):
        '''工号取消绑定 staff_id out_staff_id sys_type '''
        try:
            oracle = Oracle()
            return defer.succeed(unbondStaff(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def bondStaff(self, args):
        '''工号绑定 staff_id out_staff_id sys_type '''
        try:
            oracle = Oracle()
            return defer.succeed(bondStaff(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def abstractTax(self, args):
        '''下架'''
        try:
            oracle = Oracle()
            return defer.succeed(abstractTax(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def adjustError(self, args):
        '''错号调整'''
        try:
            oracle = Oracle()
            return defer.succeed(adjustError(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def nullifyDistri(self, args):
        '''入库发票作废'''
        try:
            oracle = Oracle()
            return defer.succeed(nullifyDistri(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def distriTax(self, args):
        '''发票下发'''
        try:
            oracle = Oracle()
            return defer.succeed(distriTax(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def instanceTax(self, args):
        '''发票上架'''
        try:
            oracle = Oracle()
            return defer.succeed(instanceTax(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def rollTax(self, args):
        '''发票回滚'''
        try:
            oracle = Oracle()
            return defer.succeed(roll(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def select(self, select_colums, sql, where_args = None):
        '''通用查询'''
        try:
            oracle = Oracle()
            return defer.succeed(select(oracle, select_colums, sql, where_args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def collectTax(self, args):
        '''发票回收'''
        try:
            oracle = Oracle()
            return defer.succeed(collectTax(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def nullifyTax(self, args):
        '''发票作废'''
        try:
            oracle = Oracle()
            return defer.succeed(nullifyTax(oracle,args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def addStaff(self, args):
        '''增加工号'''
        try:
            oracle = Oracle()
            return defer.succeed(addStaff(oracle,args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def addNote(self, args):
        '''增加附加信息 pool_id note'''
        try:
            oracle = Oracle()
            return defer.succeed(addNote(oracle,args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def addBbs(self, args):
        '''增加留言板信息 pool_id note'''
        try:
            oracle = Oracle()
            return defer.succeed(addBbs(oracle,args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def getPrivilege(self, staff_id):
        '''取得权限信息'''
        try:
            oracle = Oracle()
            return defer.succeed(getPrivilege(oracle, staff_id))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def delStaff(self, args):
        '''删除工号'''
        try:
            oracle = Oracle()
            return defer.succeed(delStaff(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def loginStaff(self, staff_id, passwd):
        '''登录工号 staff_id, passwd'''
        oracle = Oracle()
        try:
            return defer.succeed(loginStaff(oracle, staff_id = staff_id, passwd = passwd))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def getBssOrg(self, bss_org_id):
        '''获取机构下所有机构和工号树 bss_org_id'''
        try:
            oracle = Oracle()
            return defer.succeed(getBssOrgStaff(oracle, bss_org_id))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())
    def addRole(self, args):
        '''增加角色'''
        try:
            oracle = Oracle()
            return defer.succeed(addRole(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def delRole(self, args):
        '''删除角色'''
        try:
            oracle = Oracle()
            return defer.succeed(delRole(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def addRolePrivilege(self, args):
        '''增加角色权限'''
        try:
            oracle = Oracle()
            return defer.succeed(addRolePrivilege(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def delRolePrivilege(self, args):
        '''删除角色权限'''
        try:
            oracle = Oracle()
            return defer.succeed(delRolePrivilege(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def addDistri(self, args):
        '''入库'''
        try:
            oracle = Oracle()
            return defer.succeed(addDistri(oracle, **args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle)
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

class Retail():
    def __init__(self):
        oracle = Oracle()
    def getRetailInfo(self, args):
        try:
            oracle = Oracle()
            return defer.succeed(getRetailInfo(oracle, args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def changeRetail(self, args):
        try:
            oracle = Oracle()
            return defer.succeed(changeRetail(oracle, args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())

    def getOrg(self, args):
        ''' 从数据库中获取区域信息 '''
        try:
            oracle = Oracle()
            return defer.succeed(getOrg(oracle, args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())
    def getOrgID(self):
        ''' 获取id '''
        try:
            oracle = Oracle()
            return defer.succeed(getOrgID(oracle))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())
    def addOrg(self, args):
        ''' 增加org  '''
        try:
            oracle = Oracle()
            return defer.succeed(addOrg(oracle, args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())
    def delOrg(self, args):
        ''' 删除org  '''
        try:
            oracle = Oracle()
            return defer.succeed(delOrg(oracle, args))\
                .addErrback(error, oracle)\
                .addCallback(right, oracle) 
        except Warning_:
            raise Warning_(getWarningInfo())
        except Exception:
            raise Exception(getExcInfo())


if __name__ ==  "__main__":
    server = Server()
    args = {"tax_code":"123","tax_nbr":"123"}
    #server.test()
    #print hello()
    args['staff_id'] = '22'
    args['Amountlower'] = '50'
    args['BillItemList'] = ['装机费', '就是要收你钱费']

    args['Amountupper'] = '人民币（大写） 贰拾壹元零壹分'

    print server.handPrint(args)
