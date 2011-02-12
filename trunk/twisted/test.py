# -*- coding:UTF-8 -*-
from pyamf.remoting.client import RemotingService

import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s'
)


url = 'http://127.0.0.1:8001'
#url = 'http://135.33.9.54:8002'
client = RemotingService(url, logger = logging)
#client = RemotingService(url)
#service1 = client.getService('server.nullifyDistri')
#dic = {'oper_staff_id':71,'staff_id':'90'}
#print service1(dic)

#service1 = client.getService('instanceTax')
#dic = {'distri_id':1211, 'oper_staff_id':22, 'staff_id':22, 'tax_begin_nbr':'00001', 'tax_end_nbr':'50000'}
##dic = {'distri_id':1103, 'oper_staff_id':71, 'staff_id':71, 'tax_begin_nbr':'1', 'tax_end_nbr':'1'}
#print service1(dic)

service1 = client.getService('server.getOrg')
print service1('2').result
