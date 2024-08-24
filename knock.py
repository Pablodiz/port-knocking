import argparse
import re 
import ipaddress


def knock_ports(ip, puertos):
    print(ip)
    for puerto in puertos:
        print(puerto)

def validar_puertos(puertos):
    # Patrón para comprobar que los puertos: Comienzan (^) con uno o más (+) dígitos (\d), 
    # opcionalmente (?) seguidos de :tcp/:udp/:icmp y nada más ($)
    patrones = re.compile(r'^\d+(:tcp|:udp|:icmp)?$')
    for puerto in puertos:
        # Validar el formato del argumento
        if not patrones.match(puerto):
            raise argparse.ArgumentTypeError(f"The format of port '{puerto}' is invalid. It should follow the format 'port[:protocol]', where the protocol can be 'icmp', 'tcp' or 'udp'")
        # Validar que el número de puerto es válido
        puerto_num = puerto.split(':')[0]
        if not puerto_num.isdigit() or int(puerto_num) <= 0 or int(puerto_num)>65535:
            raise argparse.ArgumentTypeError(f"The port '{puerto_num}' is invalid. It should be a positive intenger lower than 65535.")
    return puertos

def validar_ip(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        raise argparse.ArgumentTypeError(f"The IP address {ip} is invalid.")
    return ip 

def main():
    # Recibir los argumentos:
    parser = argparse.ArgumentParser(description="Python script that performs port-knocking")
    parser.add_argument("-i", "--ip", required=True,  type=validar_ip, help="Target IP address")
    parser.add_argument("puertos", metavar="PORT[:PROTOCOL]", nargs="+", help="Ports to use, optionally followed by ':protocol' (tcp/udp/icmp). "\
                        "By default, the protocol is tcp.")
    
    

    try: 
        args=parser.parse_args()
        validar_puertos(args.puertos)

        # Hacer función
        knock_ports(args.ip, args.puertos)
    except Exception as e: 
        print(e)
   
if __name__=="__main__":
    main()