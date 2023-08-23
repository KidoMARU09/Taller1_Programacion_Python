def main():
    num1 = int(input("Ingrese cuatro números.\nNúmero 1: "))
    num2 = int(input("Número 2: "))
    num3 = int(input("Número 3: "))
    num4 = int(input("Número 4: "))

    maximo = max(max(num1, num2), max(num3, num4))
    minimo = min(min(num1, num2), min(num3, num4))
    numero2 = max(min(num1, num2), min(num3, num4))
    numero3 = min(max(num3, num4), max(num1, num2))

    print("El orden de menor a mayor de los números ingresados es:", minimo, ",", numero2, ",", numero3, ",", maximo)

if __name__ == "__main__":
    main()