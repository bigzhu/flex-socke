# -*- coding:UTF-8 -*-
from exp import getExcInfo
from oracle import Oracle
from call_back import right,error
from twisted.internet import defer
from instance_tax import instanceTax
from twisted.internet import threads


def right2(values, oracle = None):
    if(oracle !=  None):
        oracle.rollback()

def instanceTax2(**dic):
    '''发票上架'''
    try:
        oracle = Oracle()
        return threads.deferToThread(instanceTax(oracle, **dic))\
            .addErrback(error, oracle)\
            .addCallback(right2, oracle)
    except Exception:
        raise Exception(getExcInfo())


def test():
    instanceTax2(distri_id = 1211, oper_staff_id = 22, staff_id = 22, tax_begin_nbr = '00001', tax_end_nbr = '50000')
test()
print 1
