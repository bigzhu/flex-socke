#!/usr/bin/env python
#encoding=utf-8

import pyamf
from pyamf.amf3 import ByteArray


from twisted.internet.protocol import Protocol 
from twisted.internet.protocol import Factory
from twisted.internet import reactor


from oracle import Oracle


from login import login
from exp import getExcInfo
from exp import getWarningInfo
from exp import Warning_

class SocketProtocol(Protocol):
    ENCODING = pyamf.AMF3
    TIMEOUT = 3
    POLICY = '''
            <cross-domain-policy>
              <site-control permitted-cross-domain-policies="all"/>
              <allow-access-from domain="127.0.0.1" to-ports="8000" />
            </cross-domain-policy>
            '''
    def __init__(self):
        self.started = False
        self.encoder = pyamf.get_encoder(SocketProtocol.ENCODING)


    def connectionMade(self):
        self.factory.transports.append(self.transport)
        if len(self.factory.transports) > self.factory.max_connections:
            self.show_tip('%s个人连上来了,我干不动了,罢工!' % self.factory.max_connections)
            self.transport.loseConnection()
            return
        #持久,不断开
        #self.timeout_deferred = reactor.callLater(SocketProtocol.TIMEOUT, self.transport.loseConnection)

    def connectionLost(self, reason):
        self.factory.transports.remove(self.transport)

    def dataReceived(self, data):
        print 'transport peer =%s'% self.transport.getPeer()
        if (data.startswith('<policy-file-request/>')):
            self.transport.write(SocketProtocol.POLICY)
            print SocketProtocol.POLICY
            self.transport.loseConnection()
            return
        
        try:
            received = self.read(data)
            if(received['note'] == 'login'):
                self.login(received)
        except Warning_:
            self.alert(getWarningInfo())   

        except Exception:
            self.show_tip(getExcInfo())   

    def show_tip(self, strs, transport=None):
        obj = {}
        obj['note'] = 'show_tip'
        obj['value'] = strs
        self.write(obj, transport)
        #self.transport.loseConnection()
    def alert(self, strs):
        obj = {}
        obj['note'] = 'alert'
        obj['value'] = strs
        self.write(obj)

    def login(self, received):
        value = received['value']
        oracle = Oracle()
        return_value = {}
        return_value['note'] = 'login_over'
        return_value['value'] = login(oracle, **value)
        self.bind_staff_transport(value['staff_id'], self.transport)
        self.write(return_value)
        
    def bind_staff_transport(self, staff_id, transport):
        trans = self.factory.staff_transport_map.get(staff_id)
        if(trans is not None):
            self.show_tip('ip=%s 上有其它人用你的工号登上来了,你被踢出去了'%self.transport.getPeer().host, trans)
            trans.loseConnection()
            print 'check out'
        self.factory.staff_transport_map[staff_id] = transport
        print self.factory.staff_transport_map
        
    def tell_every_one(self, dic):
        for i in self.factory.transports:
            self.write(dic, i)
        
    def write(self, data, transport = None):
        #print 'wirte %s' % data
        self.encoder.writeElement(data)
        if(transport is None):
            self.transport.write(self.encoder.stream.getvalue())
        else:
            transport.write(self.encoder.stream.getvalue())
        self.encoder.stream.truncate()
        self.encoder.context.clear()

    def read(self, data):
        ba = ByteArray(data)
        return ba.readObject()
        
class SocketFactory(Factory):
    protocol = SocketProtocol
    max_connections = 10
    transports=[]
    staff_transport_map = {}
    #numProtocols = 0


if __name__ == '__main__':
    #host = '135.32.89.104'
    host = '127.0.0.1'
    #host = '192.168.1.4'
    app_port = 8000

    print "Running Socket AMF gateway on %s:%s" % (host, app_port)

    reactor.listenTCP(app_port, SocketFactory(), interface = host)

    reactor.run()
