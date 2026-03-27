from almacen import add_product

bodega = [{"Name": "Pan", "Stock": 5, "Unit_price": 300}, {"Name": "Cafe", "Stock": 5, "Unit_price": 500}]

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
                encontrado = True
                print("| Nombre:", pdt["Name"], "| Cantidad:", pdt["Stock"], "| Precio Unitario: $", pdt["Unit_price"], "|")
                break
            else:
                print("El producto no se encuentra en el inventario")
                return options()
    elif option == 4:
        buscar = input("Ingrese el nombre del producto a actualizar: ").capitalize().strip()

        encontrado = False

        for pdt in bodega:
         if pdt["Name"] == buscar:
            encontrado = True

            print("¿Qué desea actualizar?")
            print("1. Nombre")
            print("2. Stock")
            print("3. Precio Unitario")

            opcion_update = int(input("Seleccione una opción: "))

            if opcion_update == 1:
                nuevo_nombre = input("Nuevo nombre: ").capitalize().strip()
                pdt["Name"] = nuevo_nombre

            elif opcion_update == 2:
                nuevo_stock = int(input("Nuevo stock: "))
                pdt["Stock"] = nuevo_stock

            elif opcion_update == 3:
                nuevo_precio = float(input("Nuevo precio: "))
                pdt["Unit_price"] = nuevo_precio

            print(" Producto actualizado correctamente")
            break

        if not encontrado:
            print("Producto no encontrado")
            return options()
        
    elif option == 5:
        buscar = input("Producto a eliminar: ").capitalize().strip()

        encontrado = False

        for pdt in bodega:
            if pdt["Name"] == buscar:
                bodega.remove(pdt)
                print("Producto eliminado")
                encontrado = True
                break 

        if not encontrado:
            print("Producto no encontrado")
    elif option == 6:
        option_6()
        print (suma_total_stock)
        

def option_6 ():
    suma_total_stock = sum(d["Stock"] for d in bodega)
    return suma_total_stock
    
    

loop()