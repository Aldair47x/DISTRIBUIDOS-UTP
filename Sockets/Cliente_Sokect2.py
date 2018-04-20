import socket  
  
s = socket.socket()   
s.connect(("192.168.9.86", 4002))  

print "Amigo, ingresa un mensaje para el servidor: " 
while True:  
      mensaje = raw_input("--> ")  
      s.send(mensaje)  
      if mensaje == "Salir":  
         break  
      recibido=s.recv(1024)
      print recibido		
print "que tengas una linda tarde"  
  
s.close()  
