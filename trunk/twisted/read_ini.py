# -*- coding:UTF-8 -*-
import ConfigParser
def read_db_info():
    config = ConfigParser.ConfigParser()
    dic = {}
    cfg_file = open('im.ini','r')
    config.readfp(cfg_file)
    dic['user'] = config.get('db_info','user')
    dic['password'] = config.get('db_info','password')
    dic['tns'] = config.get('db_info','tns')
    return dic

   
if __name__ ==  "__main__":
    print read_db_info()
