#!/bin/bash

# Hay que arrancar los servicios de esta forma porque si no se intentan arrancar antes de que la máquina esté terminada, 
# por lo que no se mantendrán en ejecución cuando esté iniciado. 
service ssh start
service knockd start

# Filtrado de todo el tráfico
iptables -P INPUT DROP 
iptables -P FORWARD DROP 
iptables -P OUTPUT DROP

# Ejecuto bash para que el docker no se apague al acabar el resto de procesos
exec /bin/bash

