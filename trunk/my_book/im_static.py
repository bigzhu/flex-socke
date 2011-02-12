# -*- coding:UTF-8 -*-
from twisted.web import static, server
from twisted.application import service, internet
from twisted.application import service, strports

path = '/acct/flex4/bin'
root = static.File("/invoice/flex4/bin/")
root.putChild("InvoiceSysOperateHelp.doc", static.File(path+"/InvoiceSysOperateHelp.doc"))
root = static.File(path)
root.putChild("", static.File(path+"/InvoiceManager.html"))
root.putChild("swflash.cab", static.File(path+"/swflash.cab"))
root.putChild("swfobject.js", static.File(path+"/swfobject.js"))

application = service.Application('电子发票管理')
site = server.Site(root)
sc = service.IServiceCollection(application)

#i = internet.TCPServer(port, site)
#i.setServiceParent(sc)
#print "start static at port "+port

