# -*- coding:UTF-8 -*-
from select_ import select
from update_ import update
from insert_ import insert
from insert_ import insertLog
from datetime import datetime
import threading
from exp import Warning_
from delete import delete

def getUpdateInfo(oracle):
    '''查询信息'''
    select_colums = ['id', 'table_name', 'partition', 'need_update', 'update_count']

    select_result = select(oracle, select_colums,"from invoice.update_acct_id")
    return select_result

def getNeedUpdateInfo(oracle):
    '''查询需要update的信息'''
    select_colums = ['id', 'table_name', 'partition', 'need_update', 'update_count']

    select_result = select(oracle, select_colums,"from invoice.update_acct_id where need_update>0 and update_count is null")
    return select_result


def updateNeedUpdate(oracle, id, need_update):
    '''更新应查询的数目'''
    update(oracle = oracle, table_name = 'invoice.update_acct_id', update_dic = {'need_update':need_update}, where_dic = {'id':id})
    oracle.commit();

def updateUpdateCount(oracle, id, update_count):
    '''更实际更新的数目'''
    update(oracle = oracle, table_name = 'invoice.update_acct_id', update_dic = {'update_count':update_count}, where_dic = {'id':id})

def getNeedUpdate(oracle, table_name, partition):
    '''获取,有多少个需要更新'''
    select_colums = ['count(*)']
    if(partition == None):
        sql = 'from invoice.crm_update_acct_id c, acct.%s b where c.acct_id = b.acct_id'%table_name
    else:
        sql = 'from invoice.crm_update_acct_id c, acct.%s partition(%s) b where c.acct_id = b.acct_id'%(table_name, partition)

    select_result = select(oracle, select_colums, sql)
    return select_result[0]['count(*)']

def updateNeedTable(oracle, id, table_name, partition):
    '''更新实际的表'''
    if(partition == None):
        sql = '''
            update acct.%s a    
                set a.acct_id = 
                (select new_acct_id from invoice.crm_update_acct_id b where b.acct_id = a.acct_id) 
                where exists 
                (select null from invoice.crm_update_acct_id c where c.acct_id = a.acct_id) 
            '''%table_name
    else:
        sql = '''
            update acct.%s partition(%s) a    
                set a.acct_id = 
                (select new_acct_id from invoice.crm_update_acct_id b where b.acct_id = a.acct_id) 
                where exists 
                (select null from invoice.crm_update_acct_id c where c.acct_id = a.acct_id) 
            '''%(table_name, partition)
    row_count = oracle.execute(sql)
    updateUpdateCount(oracle, id, row_count)
    oracle.commit()

def mainNeedUpdate(oracle, id, table_name, partition):
    need_update = getNeedUpdate(oracle, table_name, partition)
    print 'need update %s'%need_update
    try:
        updateNeedUpdate(oracle, id, need_update)
    except Exception:
        print "update id = %s table_name = %s partition = %s error!!!!"%(id, table_name, partition)
        print e
        
if __name__ ==  "__main__":
    from oracle import Oracle
    oracle = Oracle()
    #检查需要update 多少
    '''
    for i in getUpdateInfo(oracle):
        oracle = Oracle()
        id = i['id']
        table_name = i['table_name']
        partition = i['partition']
        print 'check count', id,table_name,partition
        th = threading.Thread(group = None, target = mainNeedUpdate, args = (oracle, id, table_name, partition))
        th.start()
    '''
    #开始update
    for i in getNeedUpdateInfo(oracle):
        oracle = Oracle()
        id = i['id']
        table_name = i['table_name']
        partition = i['partition']
        if(partition == 'None'):
            partition = None
        print 'update acct_id ', id,table_name,partition
        th = threading.Thread(group = None, target = updateNeedTable, args = (oracle, id, table_name, partition))
        th.start()
   #oracle.commit()
