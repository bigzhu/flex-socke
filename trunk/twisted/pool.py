# -*- coding:UTF-8 -*-
from select_ import select
from insert_ import insertLog
def selectPool(oracle, select_colums, where_dic):
    '''查询pool表'''
    sql = "from pool "
    return select(oracle, select_colums, sql, where_dic)
def updatePool(oracle, update_dic, where_dic):
    '''更新pool表'''
    sql = "update pool set "
    values = ["%s = :%s" % (k, k+'_bigzhu') for k in update_dic.keys()]
    sql+= ','.join(values)
    new_update_dic = {}
    for i in update_dic.keys():
        new_update_dic[i+'_bigzhu'] = update_dic[i]
    sql+= ' where 1 = 1 '
    wheres = ["and %s = :%s" % (k, k) for k in where_dic.keys()]
    sql+= ' '.join(wheres)
    #合并两个字典
    new_update_dic.update(where_dic)

    row_count = oracle.execute(sql, new_update_dic)
    if(row_count == 0):
        raise Exception, 'update pool表记录数0'
    return row_count
def addNote(oracle, dic):
    '''增加附加信息 pool_id note oper_staff_id'''
    update_dic = {}
    update_dic['note'] = dic['note']
    where_dic = {}
    where_dic['pool_id'] = dic['pool_id']
    updatePool(oracle, update_dic, where_dic)

    where_dic = {}
    where_dic['pool_id'] = dic['pool_id']
    add_infos = {'oper':'add note'}
    add_infos['oper_staff_id'] = dic['oper_staff_id']
    add_infos['oper_date'] = '/sysdate'
    insertLog(oracle, 'pool', where_dic, add_infos)
def getNextVal(oracle):
    '''获得最新的pool_id'''
    sql = ' select pool_seq.nextval from dual '
    select_result = oracle.execute(sql)
    for select_info in select_result:
        return str(select_info[0]); 

def test_updatePool():
    from oracle import Oracle
    oracle = Oracle()

    #select_colums = ['pool_id', 'tax_code', 'tax_nbr']
    #where_dic = {"tax_code":"1111",}
    #print selectPool(oracle, select_colums, where_dic)

    where_dic = {'tax_code':'1111','tax_nbr':'0000'}
    update_dic = {'tax_code':'1111','tax_nbr':'0000'}
    print updatePool(oracle, update_dic, where_dic)
if __name__ == "__main__":
    test_updatePool()
