def main():
    caracter = input("Ingrese un caracter: ")

    if caracter.isalpha():
        if caracter.isupper():
            print("Es una letra mayúscula.")
        else:
            print("Es una letra minúscula.")
    elif caracter.isdigit():
        print("Es un número.")
    else:
        print("No es ni una letra ni un número.")

if __name__ == "__main__":
    main()
