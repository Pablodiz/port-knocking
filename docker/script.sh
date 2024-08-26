#!/bin/bash

# Bloquear todas las conexiones entrantes por defecto
iptables -P INPUT DROP 

# Hay que arrancar los servicios de esta forma porque si no se intentan arrancar antes de que la máquina esté terminada, 
# por lo que no se mantendrán en ejecución cuando esté iniciado. 
service ssh start
knockd -D

# Hago un proceso que duerma indefinidamente para que el contenedor no se apague al acabar el resto de procesos
sleep infinity
