#!/usr/bin/python
#encoding=utf-8
#file_name=oracle.py
import os
import cx_Oracle
import sys
from read_ini import read_db_info
class Oracle():
    ''' open oracle connetction get table_name and index info '''
    pool = None
    def __init__(self):
        if(Oracle.pool is None):
            getPool()
        self.db = Oracle.pool.acquire()
        self.db.autocommit = False

    def execute(self, sql, dic = None):
        try:
            sql = sql.encode('utf-8')
            cursor = self.db.cursor()
            query = None
            if(dic  ==   None):
                query = cursor.execute(sql)
            else:
                query = cursor.execute(sql, dic)
            if(query  ==   None):
                query = cursor.rowcount
                cursor.close()
            else:
                query = query.fetchall()
                cursor.close()
            return query
        except cx_Oracle.DatabaseError:
            info = sys.exc_info()
            oracle_info = str(info[1])
            print oracle_info
            if(oracle_info ==  'ORA-00028: your session has been killed\n'):
                getPool()   
                raise Exception('数据库连接出现问题，程序已自动重新连接.请重新操作')
            else:
                error = oracle_info+"\n"+sql
                raise cx_Oracle.DatabaseError(error)
    def executemany(self, sql, value):
        try:
            sql = sql.encode("utf-8")
            cursor = self.db.cursor()
            query = None
            query = cursor.executemany(sql, value)
            query = cursor.rowcount
            cursor.close()
            return query
        except cx_Oracle.DatabaseError:
            info = sys.exc_info()
            oracle_info = str(info[1])
            print oracle_info
            if(oracle_info ==  'ORA-00028: your session has been killed\n'):
                getPool()   
                raise Exception('数据库连接出现问题，程序已自动重新连接.请重新操作')
            else:
                error = oracle_info+"\n"+sql
                raise cx_Oracle.DatabaseError(error)

    def commit(self):
        self.db.commit()
    def rollback(self):
        self.db.rollback()
    def __del__(self):
        ''' 释放 '''
        Oracle.pool.release(self.db)

def getPool():
    dic = read_db_info()
    print 'start connect to %s' % dic['tns']
    os.environ["NLS_LANG"] = "AMERICAN_AMERICA.UTF8"
    Oracle.pool = cx_Oracle.SessionPool(user = dic['user'],
    password = dic['password'], dsn = dic['tns'], min = 5, max = 50,
    increment = 1, threaded = True)

def testOracle():
    oracle = Oracle()
    sql = "insert into bbs select 1,'bigzhu',1,sysdate from dual"
    print oracle.execute(sql)

def testKillSession():
    oracle = Oracle()
    sql = "insert into bbs select 1,'bigzhu',1,sysdate from dual"
    while 1:
        print oracle.execute(sql)

if __name__  ==   "__main__":
    testKillSession()
