#!/usr/bin/python
#encoding=utf-8
#file_name = hand.py
from seq import getSeq
from oracle import Oracle
from get_tax import getTax
from insert_ import insert
from use_tax import useTax

def handPrint(oracle, **args):
    '''手工发票'''
    hand = Hand(oracle, **args)
    hand.recordHandPrint()
    args['sys_type'] = 'H'
    args['state'] = 'pre-use'
    return useTax(oracle, **args)

class Hand:
    def __init__(self, oracle, **args):
        self.oracle = oracle
        self.tax_nbr = args['tax_nbr']
        self.tax_code = args['tax_code']
        self.staff_id = args['staff_id']
        self.bill_item_list = args.pop('BillItemList')
        self.hand_info = args
        self.invoice_seq_id = int(getSeq(self.oracle,'invoice_seq'))
    def recordHandPrint(self):
        self.insertHandInvoice()
        self.insertHandInvoiceDetail()
        self.insertBillItemList()
    def insertHandInvoice(self):
        '''insert table hand_invoice'''
        insert(self.oracle, 'hand_invoice', {'invoice_id':self.invoice_seq_id, 'tax_code':self.tax_code, 'tax_nbr':self.tax_nbr, 'staff_id':self.staff_id, 'sys_type':'H', 'state_date':'/sysdate'})
    def insertHandInvoiceDetail(self):
        '''insert table hand_invoice_detail'''
        invoice_detail = []
    
        for key, value in self.hand_info.items():
            dic = {'invoice_id':self.invoice_seq_id, 'region':key,
            'content':value,
            'sort':'0'}
            invoice_detail.append(dic)
    
        insert(self.oracle, 'hand_invoice_detail', invoice_detail,
        len(invoice_detail))
    def insertBillItemList(self):
        '''insert table bill_item_list'''
        bill_item = []
        for i in self.bill_item_list:
            dic = {'invoice_id':self.invoice_seq_id, 'region':'BillItemList',
            'content':i, 'sort':self.bill_item_list.index(i)}
            bill_item.append(dic)
        insert(self.oracle, 'hand_invoice_detail', bill_item,
        len(bill_item))

def testHandPrint(oracle):
    dic = getTax(oracle, 22)
    dic['staff_id'] = '22'
    dic['Amountlower'] = '50'
    dic['BillItemList'] = ['装机费', '就是要收你钱费']

    dic['Amountupper'] = '人民币（大写） 贰拾壹元零壹分'

    print handPrint(oracle, **dic)

if __name__  ==   "__main__":
    test_oracle = Oracle()
    testHandPrint(test_oracle)
    test_oracle.commit()
