from BankingSystem import BankingSystem
from Retirar import retirar

cuenta = BankingSystem()

while True:
    print("\n1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            monto = float(input("Ingrese el monto a depositar: "))
            print(cuenta.depositar(monto))
        except:
            print('Error: Debe ingresar un valor valido.')
    elif opcion == "2":
        monto = float(input("Ingrese el monto a retirar: "))
        print(retirar(cuenta, monto))

    elif opcion == "3":
        print(f"Saldo actual: ${cuenta.Consultar_saldo():,.2f}")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")
