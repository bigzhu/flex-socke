# -*- coding:UTF-8 -*-
from oracle import Oracle
def delete(oracle, table_name, where_dic = {}, and_the = ' ', count = 1):
    '''更新表'''
    sql = "delete from %s " % table_name
    where = ' where 1 = 1 '
    wheres = ["and %s = :%s" % (k, k) for k in where_dic.keys()]
    where += ' '.join(wheres)
    where += ' '+and_the

    sql += where

    row_count = oracle.execute(sql, where_dic)
    if(row_count!= count):
        raise Exception, '应delete \
        %s表%s下,实际只delete了%s,所以报错了' % (table_name, count, row_count)
    return row_count
def testDelete(oracle):
    where_dic = {'pool_id':'1303324',}
    table_name = 'pool'
    print delete(oracle = oracle, table_name = table_name, and_the = ' and \
    pool_id = 1303324')
if __name__ == "__main__":
    test_oracle = Oracle()
    testDelete(test_oracle)
    #oracle.rollback()
