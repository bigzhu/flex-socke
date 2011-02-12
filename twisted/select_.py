# -*- coding:UTF-8 -*-
from oracle import Oracle
from exp import Warning_

def select(oracle, select_colums, sql, where_dic = None, and_the = None,
bind_dic = None):
    '''select_colums list 要查的值
        sql
        where_dic 哪个字段什么条件
    '''
    values = []
    if(len(select_colums) == 0):
        raise Exception, '未设置要查哪些字段,请设定set_select_colum'
    if(where_dic is not None):
        sql += ' where 1 = 1 '
        for i in where_dic.keys():
            sql += " and %s = :%s " % (i, i)
        if(and_the is not None):
            sql += ' '+and_the+' '
    else:
        if(and_the is not None):
            sql += ' where 1 = 1 '+and_the+' '
    sql = ' select '+','.join(select_colums)+' '+sql
    if(bind_dic!= None):
        select_result = oracle.execute(sql, bind_dic)
    else:
        select_result = oracle.execute(sql, where_dic)
    for select_info in select_result:
        dic = {}
        for i in range(0, len(select_colums)):
            select_colum = select_colums[i]
            colum_name = select_colum.rsplit(' ', 1)
            colum_name = colum_name[len(colum_name)-1]
            colum_name = colum_name.rsplit('.', 1)
            colum_name = colum_name[len(colum_name)-1]
            if(select_info[i] is None):
                dic[colum_name] = select_info[i]; 
            else:
                dic[colum_name] = str(select_info[i]); 
        values.append(dic)               
    count = len(values)
    if(count>150000):
        raise Warning_,"数据有%s条记录,过大了,请缩小查询范围"%count
    if(count == 0):
        return None
    else:
        return values

def test_select():
    oracle = Oracle()
    select_colums = ['pool_id','tax_code','tax_nbr']
    where_dic = {'staff_id':'22'}
    and_the = "and tax_code = '001'"
    print select(oracle, select_colums,'from pool', where_dic, and_the)

    #print select(oracle, ['passwd'], 'from v_staff_crm', {'staff_id':'710018'})

if __name__ ==  "__main__":
    test_select()
