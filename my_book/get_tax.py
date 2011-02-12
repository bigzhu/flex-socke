#!/usr/bin/python
#encoding=utf-8
#file_name = get_tax.py
from select_ import select
from oracle import Oracle
def getTax(oracle, staff_id):
    where = {'staff_id':staff_id, 'state':'instance'}
    from_sql = '''
	            from                              
	                (select *                         
	                    from  pool            
	                        where staff_id = :staff_id
	                        and state = :state   
	                            order by to_number(tax_code), to_number(tax_nbr)              
	                )                                 
	            where rownum<2                      
            '''
    result = select(oracle, ['tax_code', 'tax_nbr'], from_sql, bind_dic = where)
    if(result == None):
        return result
    else:
        return result[0]

def test_getTax(oracle):
    print getTax(oracle, '22')
if __name__ ==  "__main__":
    oracle = Oracle()
    test_getTax(oracle)
