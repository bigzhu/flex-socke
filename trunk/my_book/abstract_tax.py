#!/usr/bin/env python
#encoding=utf-8
#file_name=abstract_tax.py
from insert_ import insertLog
from insert_ import insert
from update_ import update
from distri import getNextVal
from delete import delete

class AbstractTax:
    def __init__(self, oracle, **args):
        self.oracle = oracle

        self.tax_begin_nbr = args['tax_begin_nbr']
        self.tax_end_nbr = args['tax_end_nbr']
        self.distri_id = args['distri_id']
        self.tax_code = args['tax_code']
        self.oper_staff_id = args['oper_staff_id']
    def abstractTax(self):
        self.reversePool()
    def getReverseCount(self):
        return int(self.tax_end_nbr)-int(self.tax_begin_nbr)+1
    def reversePool(self):
        self.reverse_count = self.must_reverse_count()
        self.and_the = "and to_number(tax_nbr)> = to_number('%s') and \
        to_number(tax_nbr)< = to_number('%s')" % (self.tax_begin_nbr, self.tax_end_nbr)
        self.where_dic = {'distri_id':self.distri_id, 'tax_code':self.tax_code, 'staff_id':self.oper_staff_id}

        self.updatePool()
        self.insertPoolLog()
        self.delPool()

        def updatePool(self):
            update_dic = {'state':'abstract', 'state_date':'/sysdate'}
            self.where_dic['state'] =  'instance'

            update(oracle = oracle, table_name = 'pool', update_dic = update_dic,
            where_dic = self.where_dic, and_the = self.and_the, count = self.reverse_count)
        def insertPoolLog(self, and_the):
            self.where_dic['state'] = 'abstract', 
            add_infos = {'oper':'abstract'}
            add_infos['oper_staff_id'] = self.oper_staff_id
            add_infos['oper_date'] = '/sysdate'

            insertLog(oracle, 'pool', self.where_dic, add_infos, and_the, self.reverse_count)
        def delPool(self):
            delete(oracle = oracle, table_name = 'pool', where_dic = self.where_dic, count = self.reverse_count)

         

def abstractTax(oracle, **args):
    '''下架 distri_id, tax_code, tax_begin_nbr, tax_end_nbr, oper_staff_id'''
    poolToAbstract(oracle, **args)
    addDistrit(oracle, **args)

def poolToAbstract(oracle, **args):
    for k, v in args.items():
        exec "%s = '%s'"%(k,v)
    update_dic = {'state':'abstract','state_date':'/sysdate'}
    must_reverse_count = int(tax_end_nbr)-int(tax_begin_nbr)+1

    where_dic = {'distri_id':distri_id, 'state':'instance',
    'tax_code':tax_code, 'staff_id':oper_staff_id}

    and_the = "and to_number(tax_nbr)> = to_number('%s') and \
    to_number(tax_nbr)< = to_number('%s')"%(tax_begin_nbr, tax_end_nbr)

    update(oracle = oracle, table_name = 'pool', update_dic = update_dic, where_dic = where_dic, and_the = and_the, count = must_reverse_count)

    where_dic = {'tax_code':tax_code, 'distri_id':distri_id, 'state':'abstract', 'staff_id':oper_staff_id}
    add_infos = {'oper':'abstract'}
    add_infos['oper_staff_id'] = oper_staff_id
    add_infos['oper_date'] = '/sysdate'

    insertLog(oracle, 'pool', where_dic, add_infos, and_the, must_reverse_count)
    #删掉
    delete(oracle = oracle, table_name = 'pool', where_dic = where_dic, count = must_reverse_count)


def addDistrit(oracle, **args):
    for k, v in args.items():
        exec "%s = '%s'"%(k,v)
    #checkIfExist(oracle, tax_code = tax_code, tax_begin_nbr = tax_begin_nbr, tax_end_nbr = tax_end_nbr)

    dic = {}
    dic['distri_id'] = getNextVal(oracle)
    dic['parent_distri_id'] = distri_id
    dic['tax_code'] = tax_code
    dic['tax_begin_nbr'] = tax_begin_nbr
    dic['tax_end_nbr'] = tax_end_nbr
    #dic['sys_type'] = 'B'
    dic['state'] = 'hold'
    dic['state_date'] = '/sysdate'
    #dic['created_date'] = '/sysdate'
    dic['staff_id'] = oper_staff_id
    insert(oracle, 'distri', dic)

    where_dic = {}
    where_dic['distri_id'] = dic['distri_id']
    add_infos = {'oper':'abstract'}
    add_infos['oper_staff_id'] = oper_staff_id
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'distri', where_dic, add_infos)
    

def test_poolToReverse(oracle):
    dic = {'tax_code':'003', 'tax_begin_nbr':'0028', 'tax_end_nbr':'0030','distri_id':'1081','oper_staff_id':22 }
    poolToReverse(oracle, **dic)
def test_abstractTax(oracle):
    dic = {'tax_code':'bigzh4', 'tax_begin_nbr':'0133', 'tax_end_nbr':'0133','distri_id':'1104','oper_staff_id':22 }
    abstractTax(oracle, **dic)

if __name__ == "__main__":
    from oracle import Oracle
    oracle = Oracle()
    test_abstractTax(oracle)
    oracle.commit()
