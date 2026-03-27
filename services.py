from almacen import add_product

bodega = []

def menu():
    print("="*30)
    print("1.Add")
    print("2.View")
    print("3.Search")
    print("4.Refresh")
    print("5.Delete")
    print("6.Statistics")
    print("7.Save CSV")
    print("8.Upload CSV")
    print("9.Exit")
    print("="*30)

def loop():
    loop_var = 0
    while loop_var != 9:
        menu()
        loop_var = options()

def options():
    option = int(input(">>Seleccione una opcion: "))

    if option < 1 or option > 9:
        print("Seleccion invalida")
        print("Por favor ingrese un valor valido")
        return option
    elif option == 1:
        product = add_product()
        bodega.append(product)

    elif option == 2:
        for pdt in bodega:
            print("| Nombre:", pdt["Name"], "| Cantidad:", pdt["Stock"], "| Precio Unitario: $", pdt["Unit_price"], "|")

    elif option == 3:
        buscar = input("Ingrese nombre del producto que desea buscar: ").capitalize().strip()
        for pdt in bodega:
            if pdt["Name"] == buscar:
                print("| Nombre:", pdt["Name"], "| Cantidad:", pdt["Stock"], "| Precio Unitario: $", pdt["Unit_price"], "|")
            else:
                print("El producto no se encuentra en el inventario")
                return options()

    elif option == 4:
        print("Que desea actualizar?: ")
        print("1.Nombre")
        print("2.Stock")
        print("3.Precio Unitario")

loop()