import socket
import time

# Establece cliente UDP
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IP_servidor = ('192.xxx.xxx.xxx', 5000)  # IP y Puerto del servidor

while True:
    # Envia peticion al servidor
    miColor=input("Ingrese color, off para apagar (Verde, Azul, Rojo, Off )")
    miColor=miColor.lower()
    socket_cliente.sendto(miColor.encode(), IP_servidor)
    
    # Recibe datos del servidor
    data, addr = socket_cliente.recvfrom(1024)
    print('Datos recibidos:', data.decode())
    
