# -*- coding:UTF-8 -*-
from select_ import select
from types import StringType
from types import ListType
def insert(oracle, table_name, insert_value, count = 1):
    ''' insert sql 是根据第一行的內容来拼的.
        如果一次插入多行,且插入列与第一行不同(有更的或者更少列插入),那么不要用这个函数.
    '''
    is_list = False
    if(type(insert_value) ==  ListType):
        is_list = True
    if(is_list):
        row_count = insertMany(oracle, table_name, insert_value)
    else:
        row_count = insertOne(oracle, table_name, insert_value)

    if(row_count !=  count and count !=  0):
        raise Exception('应插%s表%s下,实际只插了%s下,所以报错了'%(table_name, count, row_count))
    return row_count

def testInsert(oracle):
    insert_value = [{'pool_id':1, 'state_date':'/sysdate'},
    {'pool_id':2,'state_date':'/sysdate'}]
    print insert(oracle, 'pool', insert_value, len(insert_value))

def insertMany(oracle, table_name, insert_value):
    sql = getSql(table_name, insert_value[0])
    for i in insert_value:
        delSysdate(i)
    return oracle.executemany(sql, insert_value)

def insertOne(oracle, table_name, insert_value):
    sql = getSql(table_name, insert_value)
    delSysdate(insert_value)
    return oracle.execute(sql, insert_value)

def delSysdate(insert_dic):
    ''' 删除 /sysdate 因为sql中用 sysdate 代替了 '''
    for key in [k for k, v in insert_dic.iteritems() if v ==  '/sysdate']:
        del insert_dic[key]

def getSql(table_name, insert_dic):
    keys = []
    values = []
    #temp_dic = insert_dic.copy()
    for k, v in insert_dic.iteritems():
        keys.append(k)
        if(v ==  '/sysdate'):
            #del insert_dic[k]
            values.append('sysdate')
        else:
            values.append(':%s'%k)

    sql = "insert into %s ( " % table_name
    sql += ','.join(keys)
    sql += ') values('
    sql += ','.join(values)
    sql += ')'
    return sql
   

def insertLog(oracle, table_name, where_dic, add_infos, and_the = '', count  = 
1):
    '''插入log表'''
    column_names = getTableColumnNames(oracle, table_name)
    columns = []
    for i in column_names:
        columns.append(i['column_name'].lower())               
    column_names_str = ''
    column_names_str += ', '.join(columns) 

    add_infos_str = ', '
    add_infos_str += ', '.join(add_infos.keys())

    #add_infos_bind = [":%s"%k for k in add_infos.keys()]
    add_infos_bind = []
    temp_dic = add_infos.copy()
    for k, v in temp_dic.iteritems():
        if(v ==  '/sysdate'):
            del add_infos[k]
            add_infos_bind.append('sysdate')
        else:
            add_infos_bind.append(':%s'%k)

    add_infos_bind_str = ', '
    add_infos_bind_str += ', '.join(add_infos_bind)

    where_dic_str = ''
    for i, j in(where_dic.items()):
        if (type(j) is StringType):
            where_dic_str += " and %s = '%s'" % (i, j)
        else:
            where_dic_str += ' and %s = %s' % (i, j)


    sql = 'insert into '+table_name+'_log('
    sql += column_names_str+add_infos_str+') select \
    '+column_names_str+add_infos_bind_str
    sql += ' from '+table_name+' where 1 = 1 '+where_dic_str
    sql += and_the
    row_count = oracle.execute(sql, add_infos)
    if(row_count !=  count and count !=  0):
        raise Exception('应插%s表%s下,实际只插了%s下,所以报错了' %
        (table_name+'_log', count, row_count))
    return row_count
def getTableColumnNames(oracle, table_name):
    '''查询表有哪些字段'''
    select_colums = ['column_name']
    sql = 'from user_tab_columns'
    where_dic = {}
    where_dic['table_name'] = table_name.upper()
    column_names = select(oracle, select_colums, sql, where_dic)
    if(column_names ==  None):
        raise Exception, '表%s不存在'%(table_name)
    return column_names

def test_insertLog(oracle):
    #select_colums = ['pool_id', 'tax_code', 'tax_nbr']
    #where_dic = {"tax_code":"1111",}
    #print selectPool(oracle, select_colums, where_dic)

    insert_dic = {'bss_org_id':'1', 'staff_id':'40071', 'staff_desc':'bigzhu'}
    table_name = 'staff'
    add_infos = {'oper':'del', 'oper_staff_id':71}
    where_dic = {'staff_id':71}
    print insertLog(oracle, table_name, where_dic, add_infos)

if __name__ ==  "__main__":
    #test_insertLog(oracle)
    testInsert()
