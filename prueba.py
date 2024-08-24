import argparse

def main():
    # Crear un parser de argumentos
    parser = argparse.ArgumentParser(description='Este es un script de ejemplo que maneja argumentos.')
    
    # Definir los argumentos
    parser.add_argument('--help', action='help', help='Muestra este mensaje de ayuda y sale.')
    parser.add_argument('--name', type=str, help='Tu nombre.')
    parser.add_argument('--age', type=int, help='Tu edad.')

    # Analizar los argumentos
    args = parser.parse_args()

    # Usar los argumentos
    if args.name:
        print(f'Hola, {args.name}!')
    if args.age:
        print(f'Tienes {args.age} años.')
    if args.name is None and args.age is None:
        print('No se proporcionaron argumentos. Usa --help para más información.')

if __name__ == "__main__":
    main()
