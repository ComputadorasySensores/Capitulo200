import network
import usocket 
import secrets
import time

LEDverde=machine.Pin(15,machine.Pin.OUT)
LEDazul=machine.Pin(13,machine.Pin.OUT)
LEDrojo=machine.Pin(14,machine.Pin.OUT)

# Conexion WiFi
red = network.WLAN(network.STA_IF)
red.active(True)
red.connect(secrets.SSID,secrets.PASSWORD)

# Espera conexion
while not red.isconnected():
    time.sleep(1)
print("Conexion realizada")
print('WiFi establecido')
print(red.ifconfig())

# Establece servidor UDP
socket_servidor = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
socket_servidor.bind((red.ifconfig()[0], 5000))
print("Servidor funcionando y en escucha")
print(red.ifconfig()[0])

while True:
    print('Esperando peticion del cliente ...')
    # Recibe peticion de cliente
    color, direccion_cliente = socket_servidor.recvfrom(1024)
    color=color.decode()
    print("Peticion del cliente:",color)
    print("Desde el cliente:",direccion_cliente)
    
    if (color=="verde"):
        LEDverde.on()
        LEDazul.off()
        LEDrojo.off()
    if (color=="azul"):
        LEDverde.off()
        LEDazul.on()
        LEDrojo.off()
    if (color=="rojo"):
        LEDverde.off()
        LEDazul.off()
        LEDrojo.on()
    if (color=="off"):
        LEDverde.off()
        LEDazul.off()
        LEDrojo.off()
    
    # Envio de datos al cliente
    data="LED "+color+" ejecutado"
    socket_servidor.sendto(data.encode(), direccion_cliente)
    print(f'Enviado al cliente {direccion_cliente}')
    time.sleep(1)
    