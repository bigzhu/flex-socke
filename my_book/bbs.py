# -*- coding:UTF-8 -*-
from oracle import Oracle
import cx_Oracle
#cx_Oracle.CLOB
def addBbs(oracle, dic):
    cursor = oracle.db.cursor()
    cursor.setinputsizes(bbs_content  =  cx_Oracle.CLOB)
    dic['bbs_content'] = str(dic['bbs_content'])
    update_sql = "update bbs b set b.bbs_content = b.bbs_content||:bbs_content \
    where trunc(b.created_date,'mi') = trunc(sysdate,'mi')"
    cursor.execute(update_sql, dic)     
    row_count = cursor.rowcount
    if(row_count ==  0):
        cursor.execute("insert into bbs(bbs_id,bbs_content, created_date)\
        values ( bbs_seq.nextval,:bbs_content,sysdate)", dic)
        row_count = cursor.rowcount
        if(row_count ==  0):
            cursor.close()
            raise Exception('未能正确插入交流信息')
    cursor.close()
    del dic['bbs_content']

def selectBbs(oracle, **args):
    bbs_id = args['bbs_id']
    values = []              
    sql = "select bbs_id, bbs_content, to_char(created_date, 'YYYY/mm/dd') \
    from bbs where trunc(created_date) = trunc(sysdate) and bbs_id> = %s order \
    by bbs_id " % bbs_id
    sql = sql.encode("utf-8")
    cursor = oracle.db.cursor()
    cursor.execute(sql)
    for rows in cursor:
        dic  =  {}
        dic['bbs_id'] = str(rows[0])
        dic['bbs_content'] = str(rows[1])
        dic['created_date'] = str(rows[2])
        values.append(dic)               
    cursor.close()
    return values

def testSelectBbs():
    oracle = Oracle()
    dic  =  {"bbs_id":9}
    print selectBbs(oracle, **dic)

def testAddBbs():
    oracle = Oracle()
    dic  =  {"bbs_content":"我汗"}
    addBbs(oracle, dic)
    oracle.commit()
if __name__  ==   "__main__":
    #test_addBbs()
    testSelectBbs()
