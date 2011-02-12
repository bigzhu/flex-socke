#!/usr/bin/python
#encoding=utf-8
#file_name = use_tax.py
from update_ import update
from insert_ import insertLog
from get_tax import getTax
from oracle import Oracle
class UseTax:
    def __init__(s, oracle, **args):
        s.oracle = oracle
        s.staff_id = args['staff_id']
        s.tax_code = args['tax_code']
        s.tax_nbr = args['tax_nbr']
        s.reprint_flag = args.get('reprint_flag')
        s.print_type = args.get('print_type')
        s.sys_type = args['sys_type']
        s.old_tax_code = args.get('old_tax_code')
        s.old_tax_nbr = args.get('old_tax_nbr')
        s.payment_id = args.get('payment_id')
        s.state = args.get('state','use')
    def useTax(s):
        s.updatePool()
        return s.get_next_tax()

    def updatePool(s):
        update_dic = {'state':s.state, 'state_date':'/sysdate', 'payment_id':s.payment_id, 'sys_type':s.sys_type, 'reprint_flag':s.reprint_flag}
        where_dic = {'staff_id':s.staff_id, 'tax_code':s.tax_code, 'tax_nbr':s.tax_nbr, 'state':'instance'}
        table_name = 'pool'
        update(s.oracle, table_name, update_dic, where_dic, need_lock = True)

        where_dic['state'] = s.state
        add_info = {'oper_staff_id':s.staff_id, 'oper':s.state, 'oper_date':'/sysdate'}
        insertLog(s.oracle, table_name, where_dic, add_info)
    def get_next_tax(s):
        result = getTax(s.oracle, s.staff_id)
        if(result == None):
            return {'tax_code':'-1', 'tax_nbr':'-1'}
        return result
def useTax(oracle, **args):
    use_tax = UseTax(oracle, **args)
    return use_tax.useTax()
def test_useTax(oracle):
    dic = getTax(oracle, 22)
    dic['staff_id'] = '22'
    dic['payment_id'] = '123456'
    dic['sys_type'] = 'H'
    print useTax(oracle, **dic)
    
if __name__ == '__main__':
    oracle = Oracle()
    test_useTax(oracle)
    oracle.commit()
