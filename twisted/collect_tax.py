# -*- coding:UTF-8 -*-
#from types import *
from staff import upperLevel
from update_ import update
from public import addZero
from public import getOperType


from distri import getDistriInfo
from distri import checkBeginEndNbr
from distri import insertDistriLog
from distri import insertDistriAsSplit
from distri import getNextVal
from exp import Warning_

class CollectTax:
    def __init__(self, oracle, **args):
        self.oracle = oracle
        self.args = args

        self.oper_staff_id = args['oper_staff_id']
        self.distri_id = args['distri_id']
        self.tax_begin_nbr = args['tax_begin_nbr']
        self.tax_end_nbr = args['tax_end_nbr']

        self.distri_info = getDistriInfo(oracle, self.distri_id)
        self.hold_staff_id = self.distri_info['staff_id']
        self.hold_tax_begin_nbr = self.distri_info['tax_begin_nbr']
        self.hold_tax_end_nbr = self.distri_info['tax_end_nbr']

        self.tax_type = getOperType(self.tax_begin_nbr, self.tax_end_nbr,
        self.hold_tax_begin_nbr, self.hold_tax_end_nbr)
    def collectTax(self):
        self.args['hold_staff_id'] = self.hold_staff_id
        if(str(self.hold_staff_id) == str(self.oper_staff_id)):
            raise Warning_,'自己回收自己的发票,没意义的,不要乱搞了'
        is_upper_staff = upperLevel(oracle = self.oracle, upper_staff =
        self.oper_staff_id, lower_staff = self.hold_staff_id)
        if(not is_upper_staff):
            raise Warning_,'工号%s没有权限操作工号%s持有的发票资源' %\
            (self.oper_staff_id, self.hold_staff_id)

        if(self.tax_type == 'a'):
            allCollect(self.oracle, oper_staff_id = self.oper_staff_id,
            distri_id = self.distri_id)
        else:
            self.partCollect()      
    def partCollect(self):
        '''部分回收
        in: type, distri_id, oper_staff_id, hold_staff_id, 
                    tax_begin_nbr, tax_end_nbr, 
                    hold_tax_begin_nbr, hold_tax_end_nbr
        '''
        self.setDistriOut()
        self.insertNewDistri()

        if(self.tax_type == 'r'):
            self.rightCollect()
        elif(self.tax_type == 'l'):
            self.leftCollect()
        elif(self.tax_type == 'm'):
            self.middleCollect()
        else:
            raise Exception,'类型错误:%s' % self.tax_type
    def setDistriOut(self):
        checkBeginEndNbr(self.tax_begin_nbr, self.tax_end_nbr, 
        self.hold_tax_begin_nbr, self.hold_tax_end_nbr)
        update_dic = {'state':'out','state_date':'/sysdate'}
        where_dic = {'distri_id':self.distri_id}
        update(self.oracle, 'distri', update_dic, where_dic)

        insertDistriLog(self.oracle, distri_id = self.distri_id, oper_staff_id =
        self.oper_staff_id, oper = 'part be collect',state = 'out')
    def insertNewDistri(self):
        #回收
        new_distri_id = getNextVal(self.oracle)

        insertDistriAsSplit(self.oracle, new_distri_id = new_distri_id,
        distri_id = self.distri_id, staff_id = self.oper_staff_id,
        tax_begin_nbr = self.tax_begin_nbr, tax_end_nbr = self.tax_end_nbr)

        insertDistriLog(oracle = self.oracle, distri_id = new_distri_id,
        oper_staff_id = self.oper_staff_id, oper = 'collect', state = 'hold')
    def rightCollect(self):
        '''左回收拆分'''
        #拆分生成原持有右边剩下的
        new_distri_id = getNextVal(self.oracle)
        split_tax_begin_nbr = addZero(len(self.tax_end_nbr),
        int(self.tax_end_nbr)+1)

        insertDistriAsSplit(self.oracle, new_distri_id = new_distri_id, distri_id =
        self.distri_id, staff_id = self.hold_staff_id, tax_begin_nbr =
        split_tax_begin_nbr, tax_end_nbr = self.hold_tax_end_nbr)
        insertDistriLog(oracle = self.oracle, distri_id = new_distri_id,
        oper_staff_id = self.oper_staff_id, oper = 'split collect',state =
        'hold')
    def leftCollect(self):      
        '''右回收'''
        #拆分生成原持有左边剩下的
        new_distri_id = getNextVal(self.oracle)
        split_tax_end_nbr = addZero(len(self.tax_begin_nbr),
        int(self.tax_begin_nbr)-1)
        insertDistriAsSplit(self.oracle, new_distri_id = new_distri_id, distri_id =
        self.distri_id, staff_id = self.hold_staff_id, 
        tax_begin_nbr = self.hold_tax_begin_nbr, tax_end_nbr =
        split_tax_end_nbr)
        insertDistriLog(oracle = self.oracle, distri_id = new_distri_id,
        oper_staff_id = self.oper_staff_id, oper = 'split collect', state =
        'hold')
    def middleCollect(self):
        '''中间回收'''
        #左边
        new_distri_id = getNextVal(self.oracle)
        split_tax_end_nbr = addZero(len(self.tax_begin_nbr),
        int(self.tax_begin_nbr)-1)

        insertDistriAsSplit(self.oracle, new_distri_id = new_distri_id, distri_id =
        self.distri_id, staff_id = self.hold_staff_id, tax_begin_nbr =
        self.hold_tax_begin_nbr , tax_end_nbr = split_tax_end_nbr)

        insertDistriLog(oracle = self.oracle, distri_id = new_distri_id,
        oper_staff_id = self.oper_staff_id, oper = 'split collect', state =
        'hold')
        #右边
        new_distri_id = getNextVal(self.oracle)
        split_tax_begin_nbr = addZero(len(self.tax_end_nbr),
        int(self.tax_end_nbr)+1)

        insertDistriAsSplit(self.oracle, new_distri_id = new_distri_id, distri_id =
        self.distri_id, staff_id = self.hold_staff_id, tax_begin_nbr =
        split_tax_begin_nbr , tax_end_nbr = self.hold_tax_end_nbr)

        insertDistriLog(oracle = self.oracle, distri_id = new_distri_id,
        oper_staff_id = self.oper_staff_id, oper = 'split collect',state =
        'hold')

def collectTax(oracle, **args):
    '''发票收回 oper_staff_id  distri_id  tax_begin_nbr  tax_end_nbr '''
    collect_tax = CollectTax(oracle, **args)
    collect_tax.collectTax()
def allCollect(oracle, distri_id, oper_staff_id):
    '''全部回收'''
    update_dic = {'state':'out','state_date':'/sysdate'}
    where_dic = {'distri_id':distri_id}
    update(oracle, 'distri', update_dic, where_dic)
    
    insertDistriLog(oracle = oracle, distri_id = distri_id, oper_staff_id =
    oper_staff_id, oper = 'be collect',state = 'out')
    
    new_distri_id = getNextVal(oracle)
    insertDistriAsSplit(oracle, new_distri_id = new_distri_id, distri_id =
    distri_id, staff_id = oper_staff_id)

    insertDistriLog(oracle = oracle, distri_id = new_distri_id, oper_staff_id =
    oper_staff_id, oper = 'collect',state = 'hold')

def test_collectTax(oracle):
    collectTax(oracle, distri_id = 999, oper_staff_id = 22, tax_begin_nbr =
    '001', tax_end_nbr = '100')
if __name__ ==  "__main__":
    from oracle import Oracle
    oracle_test = Oracle()
    test_collectTax(oracle_test)
    oracle_test.commit()
