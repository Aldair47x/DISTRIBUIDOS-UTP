import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import numpy as np
from io import StringIO
from numpy.linalg import inv
from scipy.linalg import *

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 9000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

s = xmlrpclib.ServerProxy('http://localhost:9000')

def operacion(name):
	matriz = []
	print ("Franquito")
	archivo = open(name)
	for linea in archivo:
		matriz.append(linea.strip().split())
	archivo.close()
	matrizInv=inv(matriz)
	return str(matrizInv)
	

server.register_function(operacion, 'operacion')
# Run the server's main loop
server.serve_forever()