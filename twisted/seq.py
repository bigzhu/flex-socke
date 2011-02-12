#! /usr/bin env python
#encoding=utf-8
#file_name = print.py
from select_ import select
from oracle import Oracle
def getSeq(oracle, seq_name):
    '''get seq use seq_name'''
    select_colums = ['%s.nextval id'%seq_name]
    sql = ' from dual'
    return select(oracle, select_colums, sql)[0]['id']
    
if __name__ ==  "__main__":
    oracle = Oracle()
    print getSeq(oracle, 'print_seq')
