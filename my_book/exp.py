# -*- coding:UTF-8 -*-
import traceback        
import sys
from twisted.python import log 

def getExcInfo():
    #记录twited 日志
    log.err()

    info = sys.exc_info()
    #print type(info[0])
    exp_type =  str(info[0])
    if(info[0] == Warning_):
        '是waring'
    print type(info[0])
    print exp_type
    exc_traceback = sys.exc_info()[2]
    exc_traceback = traceback.extract_tb(exc_traceback)
    error = ""
    for file, line_no, function, exception_info in exc_traceback:
        #error_info_tmp = error_info.rsplit(',')[1].rsplit("'")[1]
        #不需要函数名,会暴露
        #function = ""
        #if(function ==  "<module>"):
        #    function = ""
        #不需要抛出异常的函数
        exception_info = ""

        #不需要绝对地址,只要文件名
        file = file.rsplit("/")[-1]

        #print file
        error += "\n"+file+":"+str(line_no)+" 函数:"+function+" "+ exception_info
    error_info = str(info[1])
    error  = "\n"+exp_type+ error+ "\n"+error_info
    return error

def test_getExcInfo():
    try:
        distri_id = '7892392'
        raise Exception('根据distri_id big = %s找不到发票持有者'%distri_id)
        #pool = cx_Oracle.SessionPool(user = user, password = password, dsn = tns, min = 1, max = 200, increment = 10)
        #oracle = Oracle(pool)
        #sql = "select * from ddistri"
        #select_result = oracle.execute(sql)
        #print select_result
    except Exception:
        #print type(e)
        #print e.args
        #x = e
        #print x
        #raise e
        #raise
        print getExcInfo()

class Warning_(Exception):
    pass

def getWarningInfo():
    info = sys.exc_info()
    error_info = str(info[1])
    return error_info
def test_getWarningInfo():
    try:
        distri_id = '7892392'
        raise Warning_('根据distri_id big = %s找不到发票持有者'%distri_id)
    except Warning_:
        print getWarningInfo()

if __name__ ==  '__main__':
    #test_getExcInfo()
    test_getWarningInfo()
