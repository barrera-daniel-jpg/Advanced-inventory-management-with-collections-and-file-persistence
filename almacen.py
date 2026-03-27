from collections import Counter

def add_product():
    
    valid = 0
    while valid != 1:
        name = str(input("Ingrese el nombre del producto: ")).capitalize().strip()
        if name == "":
            print("El nombre no puede estar vacío")
        else:
            valid = 1

    
    valid = 0
    while valid != 1:
        try:
            stock = int(input("Ingrese el stock: "))
            if stock < 0:
                print("El stock no puede ser negativo")
            else:
                valid = 1
        except ValueError:
            print("Error: El stock debe ser un número entero")

  
    valid = 0
    while valid != 1:
        try:
            unit_price = float(input("Ingrese el precio unitario: "))
            if unit_price < 0:
                print("El precio no puede ser negativo")
            else:
                valid = 1
        except ValueError:
            print("Error: El precio debe ser un número")

    product_and_more = {"Name": name, "Stock": stock, "Unit_price": unit_price}
    print(f"El producto registrado satisfactoriamente")
    return product_and_more

def calcular_estadisticas ():
    contador = Counter(bodega)
    unidades_totales = contador
    print(unidades_totales)
    return unidades_totales