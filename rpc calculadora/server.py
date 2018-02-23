import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer



class superCalculadora(xmlrpclib.Transport):
    
    def division_remota(self, a,b):
        return a/b

    def multiplicacion_remota(self, a,b):
        return a*b

    def resta_remota(self, a, b):
        return a-b

    def	suma_remota(self, a, b):
	return a+b


p = superCalculadora()
"""
server = xmlrpclib.ServerProxy('http://time.xmlrpc.com/RPC2', transport=p)
print server.currentTime.getCurrentTime()
"""	
server = SimpleXMLRPCServer(("192.168.9.80", 8001))
server.register_instance(superCalculadora())
print "soy el servidor y estoy corriendo por el pueto 8001"
server.serve_forever()


