#Ángel Montenegro/1053124
#Christopher García/1265924

pedido = {
    "cliente": "",
    "nit": "",
    "licuado": "Licuado de fresa con leche deslactosada sin azúcar (Tamaño: Normal)",
    "precio original": 10.00,
    "azúcar": 0,
    "leche": "Leche deslactosada",
    "tamaño": "Normal",
    "precio total": 10.00
}

pedido["cliente"] = input("Ingrese su nombre completo: ")
pedido["nit"] = input("Ingrese su NIT: ")

while True:
    print("Menú:")
    print("1. Ver información del pedido")
    print("2. Agregar azúcar")
    print("3. Modificar leche")
    print("4. Agrandar")
    print("5. Confirmar")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Detalle del pedido:")
        for key, value in pedido.items():
            print(f"{key}: {value}")

    elif opcion == "2":
        if pedido["azúcar"] < 2:
            pedido["azúcar"] += 1
            pedido["precio total"] += 0.50
            print("Se agregó una cucharada de azúcar.")
            print(f"Cantidad de azúcar: {pedido['azúcar']}")
            print(f"Cantidad a cobrar por azúcar: Q{pedido['azúcar'] * 0.50}")
        else:
            print("No se puede agregar más azúcar.")

    elif opcion == "3":
        print("\nOpciones de leche:")
        opciones_leche = ["Solo agua", "Leche deslactosada", "Leche entera", "Leche de soya"]
        for i, leche in enumerate(opciones_leche):
            print(f"{i + 1}. {leche}")
        seleccion = int(input("Seleccione una opción: "))
        if 1 <= seleccion <= 4:
            leches = ["", "Sin leche", "Leche deslactosada", "Leche entera", "Leche de soya"]
            pedido["leche"] = leches[seleccion]
            if seleccion == 1:
                pedido["precio total"] -= 2.00
            elif seleccion == 4:
                pedido["precio total"] += 3.00
            print("Tipo de leche modificado con éxito.")
        else:
            print("Opción inválida.")

    elif opcion == "4":
        if pedido["tamaño"] == "Normal":
            pedido["tamaño"] = "Grande"
            pedido["precio total"] *= 1.05
            print("El tamaño del licuado se ha agrandado.")
        else:
            print("El tamaño del licuado ya está en grande.")

    elif opcion == "5":
        print("Detalle del pedido final:")
        for key, value in pedido.items():
            print(f"{key}: {value}")
        print(f"Precio total: Q{pedido['precio total']}")
        print("¡Gracias por su compra!")
        break

    else:
        print("Por favor, seleccione una opción válida.")
