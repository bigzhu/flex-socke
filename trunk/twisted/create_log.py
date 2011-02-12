# -*- coding:UTF-8 -*-
import sys
if(len(sys.argv) == 1):
    raise Exception,'要输入表名'
table_name = sys.argv[1]
print ''
print 'create table %s_log as select * from %s where \
rownum<0;' % (table_name,table_name)
print ''' -- Add/modify columns 
alter table %s_LOG add oper_staff_id NUMBER(12);
alter table %s_LOG add oper VARCHAR2(100);
alter table %s_LOG add oper_date date;
-- Add comments to the columns 
comment on column %s_LOG.oper_staff_id
  is '操作工号';
comment on column %s_LOG.oper
  is '操作';
comment on column %s_LOG.oper_date
  is '操作日期';
  '''%(table_name, table_name, table_name, table_name, table_name, table_name)
