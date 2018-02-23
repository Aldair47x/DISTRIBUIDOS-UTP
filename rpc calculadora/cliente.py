import xmlrpclib  
a =input('Ingrese el primer numero: ')
b=input('Ingrese el segundo numero: ')
proxy = xmlrpclib.ServerProxy("http://192.168.9.80:8001/")

print "La suma es: " +str(proxy.resta_remota(a,b))
