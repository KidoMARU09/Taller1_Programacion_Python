def main():


    a = float(input("Ingrese el lado a: "))
    b = float(input("Ingrese el lado b: "))
    c = float(input("Ingrese el lado c: "))

    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c and c == a:
            print("El triángulo es equilátero.")
        elif a == b or a == c or b == c:
            print("El triángulo es isósceles.")
        elif a != b and a != c and b != c:
            print("El triángulo es escaleno.")
    else:
        print("Las medidas ingresadas no cumplen la desigualdad triangular.")

if __name__ == "__main__":
    main()


