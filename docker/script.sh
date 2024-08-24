#!/bin/bash

# Bloquear todas las conexiones al puerto 22 por defecto
iptables -A INPUT -p tcp --dport 22 -j DROP

# Hay que arrancar los servicios de esta forma porque si no se intentan arrancar antes de que la máquina esté terminada, 
# por lo que no se mantendrán en ejecución cuando esté iniciado. 
service ssh start
knockd -D

# Ejecuto bash para que el docker no se apague al acabar el resto de procesos
sleep infinity