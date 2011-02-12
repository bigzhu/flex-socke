#!/usr/bin/python
#encoding=utf-8
#file_name=public.py
def addZero(length, short):
    value = str(short)
    while(len(value)<length):
        value = '0'+value
    return value

def getOperType(tax_begin_nbr, tax_end_nbr, hold_tax_begin_nbr,
hold_tax_end_nbr):
    '''取得号段类型
    in:     tax_begin_nbr, tax_end_nbr, hold_tax_begin_nbr, hold_tax_end_nbr
    return: tax_type
    '''
    if(tax_begin_nbr == hold_tax_begin_nbr and tax_end_nbr == hold_tax_end_nbr):
        type = 'a'
    elif(tax_begin_nbr == hold_tax_begin_nbr):
        type = 'r'
    elif(tax_end_nbr == hold_tax_end_nbr):
        type = 'l'
    else:
        type = 'm'
    return type

if __name__  ==   "__main__":
    pass
