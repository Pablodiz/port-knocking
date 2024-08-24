# port-knocking
Proyecto creado para ver el funcionamiento del mecanismo *port knocking*, creando una herramienta de python que lo ejecute y un contenedor de docker que lo acepte.  

# Docker
Para probar el uso del script, he decidido hacer un contenedor de docker sobre el que poder hacer port-knocking. 

Tras recibir cierta secuencia de puertos, el contenedor permitirá el acceso por ssh.

Para construir la imagen y ejecutar el contenedor: 
```
cd docker
sudo docker build -t knocking .
sudo docker run -itd --privileged --rm --name knock knocking
```

Haciendo nmap, podemos ver que el puerto 22 está filtrado: 

![alt text](image.png)