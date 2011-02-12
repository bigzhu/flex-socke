# -*- coding:UTF-8 -*-
from twisted.web import resource, server

from pyamf.remoting.gateway.twisted import TwistedGateway
from pyamf.remoting.gateway import expose_request



from exp import getExcInfo
from oracle import Oracle
from call_back import right,error
from twisted.internet import defer
from twisted.internet import threads

import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

import logging
logging.basicConfig(level = logging.ERROR, format = '%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s')

from server import Server
server = Server()
services = {
    "get_bss_org":server.getBssOrg,
    "select":server.select,
    "add_bbs":server.addBbs,
    'roll_tax':server.rollTax,
    'get_privilege':server.getPrivilege,
    'instanceTax':instanceTax,
    'server':server
}

gateway = TwistedGateway(services, logger = logging, expose_request = False,debug = True)
root = resource.Resource()
root.putChild('', gateway)

from twisted.internet import reactor
from twisted.web import resource, server
from twisted.application import service, strports
from im import root
from wsgi import site

port = 8002
print 'Running AMF gateway on http://localhost:%s'%port
reactor.suggestThreadPoolSize(5000)
#reactor.listenTCP(port, server.Site(root))
#reactor.run()
application = service.Application('Invoice Mananger Remoting Server')
server = strports.service('tcp:%s'%port, server.Site(root))
server.setServiceParent(application)

