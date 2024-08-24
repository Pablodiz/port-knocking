FROM ubuntu:20.04

# Instalación de paquetes necesarios 
RUN apt-get update && apt-get upgrade -y && \ 
    apt-get install iptables knockd openssh-server -y \ 
     && apt-get clean && \
     rm -rf /var/lib/apt/lists/*

# Fichero de configuración de knockd  
COPY knockd.conf /etc/knockd.conf

# Crear un usuario al que conecta, con contraseña password (hay que pasársela encriptada)
RUN useradd -m -p $(openssl passwd -1 password) user

# Copio y permito la ejecución del script
COPY script.sh script.sh 
RUN chmod +x script.sh 

EXPOSE 22 2000 3000 4000

CMD ["./script.sh"]