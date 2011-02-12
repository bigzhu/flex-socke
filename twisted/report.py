# -*- coding:UTF-8 -*-
from select_ import select
def initStaffId(oracle, bss_org_id):
    sql = '''
    insert into staff_report select staff_id from staff where bss_org_id in
          (select bss_org_id
          from bss_org
            connect by prior bss_org_id =  bss_parent_org_id
            start with bss_org_id       = %s
          )

    '''%bss_org_id
    row_count = oracle.execute(sql)
    if(row_count == 0):
        raise Exception, '机构%s下没有工号'%bss_org_id

def getHoldTaxPool(oracle, report_dic):
    sql = '''
            select staff_id, tax_code, min(tax_nbr), max(tax_nbr)
              from (select staff_id,
                           tax_code,
                           tax_nbr,
                           to_number(tax_nbr) -
                           (row_number() over(partition by staff_id order by tax_nbr)) dif
                      from pool
                     where staff_id in (select staff_id from staff_report))
             group by staff_id, tax_code, dif
    '''
    report_dic = {}
    for i in oracle.execute(sql):
        staff_tax_code = (i[0],i[1])
        #tax_begin_end = '%s--%s'%
        report_dic[staff_tax_code] = {'staff_id':i[0], 'tax_code':i[1], 'tax_begin_nbr':i[2], 'tax_end_nbr':i[3]}
    return report_dic

def getStaffInfo(oracle):
    sql = '''
    select staff_id,
          staff_desc,
          b.name
        from staff s,
          bss_org b
        where s.bss_org_id = b.bss_org_id
        and s.staff_id in(select staff_id from staff_report)
    '''
    report_dic = {}
    for i in oracle.execute(sql):
        report_dic[i[0]] = {'staff_id':i[0], 'staff_name':i[1], 'bss_org_name':i[2]}
    print report_dic

def test_getStaffInfo(oracle):
    getStaffInfo(oracle)

if __name__ == "__main__":
    from oracle import Oracle
    oracle = Oracle()
    initStaffId(oracle,8760801)
    test_getStaffInfo(oracle)
    oracle.rollback()
