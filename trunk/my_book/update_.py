# -*- coding:UTF-8 -*-
from oracle import Oracle
def update(oracle, table_name, update_dic, where_dic = {}, and_the = ' ', count
 =  1, need_lock = False):
    '''更新表'''
    #时间
    temp_dic = update_dic.copy()
    sysdate = []
    for k, v in temp_dic.iteritems():
        if(v ==  '/sysdate'):
            del update_dic[k]
            sysdate.append(' %s = sysdate '%k)

    sql = "update %s set " % table_name
    values = ["%s = :%s" % (k, k+'_bigzhu') for k in update_dic.keys()]
    values.extend(sysdate)
    sql += ','.join(values)
    new_update_dic = {}
    for i in update_dic.keys():
        new_update_dic[i+'_bigzhu'] = update_dic[i]
    where = ' where 1 = 1 '
    wheres = ["and %s = :%s" % (k, k) for k in where_dic.keys()]
    where += ' '.join(wheres)
    where += ' '+and_the

    sql += where
    #合并两个字典
    new_update_dic.update(where_dic)

    if(need_lock):
        lock(oracle, table_name, where, count, where_dic)

    row_count = oracle.execute(sql, new_update_dic)
    if(row_count !=  count and count !=  0):
        raise Exception('应update \
        %s表%s下,实际update了%s,所以报错了'%(table_name, count, row_count))
    return row_count
def lock(oracle, table_name, where, count, where_dic):
    sql = 'select * from %s %s for update nowait' % (table_name, where)
    query = oracle.execute(sql, where_dic)
    if(len(query) !=  count and len(query) !=  0):
        raise Exception, '锁住记录数过多%s'%len(query)
def test_update():
    oracle = Oracle()
    where_dic = {'staff_id':'71',}
    update_dic = {'staff_desc':'bigzhu','state_date':'/sysdate'}
    table_name = 'staff'
    print update(oracle = oracle, table_name = table_name, update_dic  = 
    update_dic, and_the = ' and staff_id = 71', need_lock = True)
    #oracle.commit()   
if __name__ ==  "__main__":
    test_update()
    #oracle.rollback()
