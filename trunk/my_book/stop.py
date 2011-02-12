# -*- coding:UTF-8 -*-
import os
import re
import sys
def get_pid(pid_name):
    file_name = pid_name+'.pid'
    f = open(file_name)
    pid = f.read()
    print "get %s's pid = %s"%(file_name,pid)
    f.close()
    return pid
def kill(pid,type = ''):
    cmd = "kill %s %s"%(type,pid)
    print cmd
    os.system(cmd)
def rm(file_name):
    cmd = "rm -f %s "%(file_name)
    print cmd
    os.system(cmd)

#是否还在
def check(pid):
    cmd = 'ps -ef|grep %s'%pid
    f = os.popen(cmd)
    txt = f.read()
    f.close()
    regex = re.compile(r'python')
    still_run = regex.findall(txt)
    if(len(still_run)!= 0):
        return True
    else:
        return False
if __name__ ==  "__main__":
    if(len(sys.argv) == 1):
        raise Exception,'python stop.py pid名字'

    pid_name = sys.argv[1]

    pid = get_pid(pid_name)
    kill(pid)
    while(check(pid)):
        kill(pid,'-9')
    print '进程%s已经不存在'%pid
    rm(pid_name+'.pid')
