# -*- coding:UTF-8 -*-
from select_ import select
from insert_ import insertLog
from update_ import update
from exp import Warning_

class AdjustError:
    def __init__(self, oracle, **args):
        self.oracle = oracle
        self.args = args

        self.tax_code = args['tax_code']
        self.tax_nbr = args['tax_nbr']
        self.new_tax_code = args['new_tax_code']
        self.new_tax_nbr = args['new_tax_nbr']
        self.oper_staff_id = args['oper_staff_id']

        self.and_the = "and state in('use', 'reverse', 'instance', 'abdicate')"
        result = checkIsInstance(self.oracle, self.tax_code, self.tax_nbr,
        self.and_the)
        self.pool_id = result['pool_id']
        self.state = result['state']
        self.sys_type = result['sys_type']

        result = checkIsInstance(oracle, self.new_tax_code, self.new_tax_nbr,
        self.and_the)
        self.be_pool_id = result['pool_id']
        self.be_state = result['state']
        self.be_sys_type = result['sys_type']

    def adjustError(self):
        self.checkCanAdjust(self.state)
        self.updatePool()
        self.updateInvoice()
    def checkCanAdjust(self, state):
        if(state !=  'use' and state !=  'reverse' and state !=  'abdicate'):
            raise Warning_,"发票代码 %s  发票号码%s 还未使用. 不用调整" % \
            (self.tax_code, self.tax_nbr)
    def updatePool(self):
        table_name = 'pool'
        #将要调的发票先置-1
        update_dic = {'tax_nbr':'-1', 'tax_code':'-1'}
        where_dic = {'pool_id':self.pool_id, 'tax_code':self.tax_code,
        'tax_nbr':self.tax_nbr}
        update(oracle = self.oracle, table_name = table_name, update_dic  = 
        update_dic, where_dic = where_dic, and_the = self.and_the)

        #将被影响的发票置之
        update_dic = {'tax_nbr':self.tax_nbr, 'tax_code':self.tax_code}
        where_dic = {'pool_id':self.be_pool_id, 'tax_code':self.new_tax_code,
        'tax_nbr':self.new_tax_nbr}
        update(oracle = self.oracle, table_name = table_name, update_dic  = 
        update_dic, where_dic = where_dic, and_the = self.and_the)

        where_dic = {'pool_id':self.be_pool_id}
        add_infos = {'oper':'adjust', 'oper_staff_id':self.oper_staff_id,
        'oper_date':'/sysdate'}
        insertLog(self.oracle, table_name, where_dic, add_infos)

        #将-1的置之
        update_dic = {'tax_nbr':self.new_tax_nbr,
        'tax_code':self.new_tax_code}
        where_dic = {'pool_id':self.pool_id, 'tax_code':'-1', 'tax_nbr':'-1'}
        update(oracle = self.oracle, table_name = table_name, update_dic  = 
        update_dic, where_dic = where_dic, and_the = self.and_the)


        where_dic = {'pool_id':self.pool_id}
        add_infos = {'oper':'adjust', 'oper_staff_id':self.oper_staff_id,
        'oper_date':'/sysdate'}
        insertLog(self.oracle, table_name, where_dic, add_infos)       
    def updateInvoice(self):
        table_name = 'e_invoice'
        be_table_name = 'e_invoice'
        if(self.sys_type ==  'C'):
            table_name = 'e_invoice_crm'
        elif(self.sys_type ==  'B'):
            table_name = 'e_invoice_bill'
        else:
            raise Exception('取到的系统类型为%s,不正确'%self.sys_type)

        if(self.be_state ==  'use' or self.be_state ==  'reverse' or
            self.be_state ==  'abdicate'):
            if(self.be_sys_type ==  'C'):
                be_table_name = 'e_invoice_crm'
            elif(self.sys_type ==  'B'):
                be_table_name = 'e_invoice_bill'
            else:
                raise Exception('取到的系统类型为%s,不正确'%self.be_sys_type)

            update_dic = {'tax_nbr':'-1', 'tax_code':'-1'}
            where_dic = {'tax_code':self.tax_code, 'tax_nbr':self.tax_nbr}
            update(oracle = self.oracle, table_name = table_name, update_dic  = 
            update_dic, where_dic = where_dic)

            update_dic = {'tax_nbr':self.tax_nbr, 'tax_code':self.tax_code}
            where_dic = {'tax_code':self.new_tax_code,
            'tax_nbr':self.new_tax_nbr}
            update(oracle = self.oracle, table_name = be_table_name, update_dic
            = update_dic, where_dic = where_dic)


            dic = {'pool_id':self.be_pool_id, 'new_tax_code':self.tax_code,
            'new_tax_nbr':self.tax_nbr, 'tax_code':self.new_tax_code,
            'tax_nbr':self.new_tax_nbr, 'oper_staff_id':self.oper_staff_id}
            adjustLog(self.oracle, dic)

            update_dic = {'tax_nbr':self.new_tax_nbr,
            'tax_code':self.new_tax_code}
            where_dic = {'tax_code':'-1', 'tax_nbr':'-1'}
            update(oracle = self.oracle, table_name = table_name, update_dic  = 
            update_dic, where_dic = where_dic)

            self.args['pool_id'] = self.pool_id
            adjustLog(self.oracle, self.args)
        else:
            sql = "update %s p set p.tax_code = '%s', p.tax_nbr = '%s' where \
            tax_code = '%s' and tax_nbr = '%s'" % (table_name,
            self.new_tax_code, self.new_tax_nbr, self.tax_code, self.tax_nbr)
            row_count = self.oracle.execute(sql)
            if(row_count !=  1):
                raise Exception('update %s表记录数%s'%(table_name, row_count))
            self.args['pool_id'] = self.pool_id
            adjustLog(self.oracle, self.args)

def adjustError(oracle, **args):
    adjust_error = AdjustError(oracle, **args)
    adjust_error.adjustError()
def checkIsInstance(oracle, tax_code, tax_nbr, and_the):
    '''检查发票是否都上架了'''
    select_colums = ['pool_id', 'state', 'sys_type']
    sql = "from pool where tax_code = '%s' and tax_nbr = '%s' %s" % (tax_code,
    tax_nbr, and_the)
    result = select(oracle, select_colums, sql)
    if(result ==  None):
        raise Warning_('待调整发票 tax_code = %s, tax_nbr = %s 未能找到,\
        请确定是否已上架.'%(tax_code, tax_nbr))
    return result[0]

def adjustLog(oracle, dic):
    sql = '''
    insert
    into adjust_log
      (
        adjust_id,
        invoice_id,
        old_invoice_id,
        tax_code,
        tax_nbr,
        old_tax_code,
        old_tax_nbr,
        oper_date,
        oper_staff_id,
        pool_id,
        old_pool_id
      )
       values
      (
        adjust_seq.nextval,
        null,
        null,
        :new_tax_code,
        :new_tax_nbr,
        :tax_code,
        :tax_nbr,
        sysdate,
        :oper_staff_id,
        :pool_id,
        null
      ) 
    '''
    row_count = oracle.execute(sql, dic)
    if(row_count !=  1):
        raise Exception('insert adjust_log表记录数%s'%row_count)

def testAdjustError():
    from oracle import Oracle
    oracle = Oracle()

    dic = {'tax_code':'300', 'tax_nbr':'0012', 'new_tax_code':'003',
    'new_tax_nbr':'0021', 'oper_staff_id':22}
    adjustError(oracle, **dic)
if __name__ ==  "__main__":
    testAdjustError()
