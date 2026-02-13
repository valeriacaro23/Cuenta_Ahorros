class BankingSystem:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto <= 0:
            return 'El monto debe ser mayor que 0.'


        self.saldo += monto
        return f'Depósito exitoso. Nuevo saldo: ${self.saldo:,.2f}'

    def Consultar_saldo(self):
        return self.saldo    