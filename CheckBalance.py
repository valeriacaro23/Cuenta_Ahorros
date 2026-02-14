from BankingSystem import BankingSystem

cuenta = BankingSystem()

while True:
    print("\n1. Depositar")
    print("2. Consultar saldo")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            monto = float(input("Ingrese el monto a depositar: "))
            print(cuenta.depositar(monto))
        except:
            print('Error: Debe ingresar un valor valido.')
    elif opcion == "2":
        print("Saldo actual:", cuenta.Consultar_saldo())

    elif opcion == "3":
        
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")

