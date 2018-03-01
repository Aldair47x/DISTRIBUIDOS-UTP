import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

s = xmlrpclib.ServerProxy('http://localhost:9000')
					
def main():
	while True:	
		name=raw_input("Ingrese el nombre del archivo: ")
		result=s.operacion(name)
		print(result)
		
main()