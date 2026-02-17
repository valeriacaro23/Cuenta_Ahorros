def retirar(cuenta, monto):
    if monto <= 0:
        return 'El monto debe ser mayor que 0.'

    if monto > cuenta.saldo:
        return f'Fondos insuficientes. Saldo actual: ${cuenta.saldo:,.2f}'

    cuenta.saldo -= monto
    return f'Retiro exitoso. Nuevo saldo: ${cuenta.saldo:,.2f}'
