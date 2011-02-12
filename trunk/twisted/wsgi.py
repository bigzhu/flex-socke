# -*- coding:UTF-8 -*-
from pyamf.remoting.gateway.wsgi import WSGIGateway
from pyamf.remoting.gateway import expose_request

from twisted.web import server
from twisted.web.wsgi import WSGIResource
from twisted.python.threadpool import ThreadPool
from twisted.internet import reactor
from twisted.application import service, strports
        
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 


import logging
logging.basicConfig(level = logging.ERROR, format = '%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s')
#logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s')

from im_server import Server
im_server = Server()
from im_server import Retail
retail = Retail()
services = {
    'server':im_server,
    'retail':retail
}

# Create a dictionary mapping the service namespaces to a function
# or class instance

# Create and start a thread pool,
wsgiThreadPool = ThreadPool()
wsgiThreadPool.start()

# ensuring that it will be stopped when the reactor shuts down
reactor.addSystemEventTrigger('after', 'shutdown', wsgiThreadPool.stop)

# PyAMF gateway
gateway = WSGIGateway(services, logger = logging, expose_request = False, debug = True)


# Create the WSGI resource
wsgiAppAsResource = WSGIResource(reactor, wsgiThreadPool, gateway)
site = server.Site(wsgiAppAsResource)


reactor.suggestThreadPoolSize(5000)
# Hooks for twistd
application = service.Application('Invoice Mananger Remoting Server')
#server = strports.service('tcp:8002', site)
#server.setServiceParent(application)

