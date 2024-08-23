# port-knocking

# Docker
Para probar el uso del script, he decidido hacer un contenedor de docker sobre el que poder hacer port-knocking. 

Tras recibir cierta secuencia de puertos, el contenedor permitirá el acceso por ssh.

Para construir la imagen y ejecutar el contenedor: 
```
sudo docker build --no-cache -t knocking:1.0 .
sudo docker run -itd --privileged --rm --name knock knocking
```