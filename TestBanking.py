import unittest
from BankingSystem import BankingSystem
from Retirar import retirar


class TestBankingSystem(unittest.TestCase):
    def setUp(self):
          self.cuenta = BankingSystem()

# prueba saldo inicia #

    def test_saldo_inicial_por_defecto(self):
        self.assertEqual(self.cuenta.Consultar_saldo(), 0)

    def test_saldo_inicial_personalizado(self):
        cuenta = BankingSystem(saldo_inicial=500)
        self.assertEqual(cuenta.Consultar_saldo(), 500)

# PRUEBAS UNITARIAS DEPOSITAR

# Validar la comulación de deositos
    def test_depositar_multiples_veces(self):
        self.cuenta.depositar(100)
        self.cuenta.depositar(250)
        self.assertEqual(self.cuenta.Consultar_saldo(), 350)

# Al depositar 0 el sistema no debe permitirlo 
    def test_depositar_monto_cero(self):
        resultado = self.cuenta.depositar(0)
        self.assertEqual(resultado, 'El monto debe ser mayor que 0.')

#Depositar valores negativos
    def test_depositar_monto_negativo(self):

        resultado = self.cuenta.depositar(-100)
        self.assertEqual(resultado, 'El monto debe ser mayor que 0.')


 # PRUEBAS UNITARIAS RETIRAR

# Reducir saldo
    def test_retirar_monto_valido(self):
        self.cuenta.depositar(500)
        retirar(self.cuenta, 200)
        self.assertEqual(self.cuenta.Consultar_saldo(), 300)

#retirar saldo disponible
    def test_retirar_todo_el_saldo(self):
        self.cuenta.depositar(100)
        resultado = retirar(self.cuenta, 100)
        self.assertEqual(self.cuenta.Consultar_saldo(), 0)
        self.assertIn('exitoso', resultado.lower())

# Retirar monto mayor, mostrar mensaje de saldo insuficiente
    def test_retirar_fondos_insuficientes(self):
        """Retirar más del saldo disponible debe retornar mensaje de error."""
        self.cuenta.depositar(100)
        resultado = retirar(self.cuenta, 500)
        self.assertIn('insuficientes', resultado.lower())

# Al retirar valor 0 mostrar mensaje de error
    def test_retirar_monto_cero(self):
        resultado = retirar(self.cuenta, 0)
        self.assertEqual(resultado, 'El monto debe ser mayor que 0.')

# retirar monto negativo mostrar error
    def test_retirar_monto_negativo(self):
        resultado = retirar(self.cuenta, -50)
        self.assertEqual(resultado, 'El monto debe ser mayor que 0.')


#retirar saldo muestre saldo actual
    def test_retirar_retorna_mensaje_con_nuevo_saldo(self):
        self.cuenta.depositar(400)
        resultado = retirar(self.cuenta, 100)
        self.assertIn('300.00', resultado)


    # PRUEBAS CONSULTAR SALDO

    # Conusltar saldo exitoso
    def test_consultar_saldo_retorna_valor_correcto(self):
        self.cuenta.depositar(750)
        self.assertEqual(self.cuenta.Consultar_saldo(), 750)