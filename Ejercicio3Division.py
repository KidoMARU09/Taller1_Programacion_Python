def main():
    a = int(input("Ingrese dos números enteros\nDividendo: "))
    b = int(input("Divisor: "))
    residuo = 0
    cociente = 0

    if b != 0:
        residuo = a % b
        cociente = a // b
        if residuo == 0:
            print("La división es exacta.")
            print("Cociente:", cociente)
            print("Residuo:", residuo)
        else:
            print("La división no es exacta.")
            print("Cociente:", cociente)
            print("Residuo:", residuo)
    else:
        print("La división es indeterminada")

if __name__ == "__main__":
    main()