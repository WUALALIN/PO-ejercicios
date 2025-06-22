
class CuentaBancaria:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        return False


class Cajero:
    def retirar_dinero(self, cuenta, monto):
        if cuenta.retirar(monto):
            return f"Retiro exitoso. Saldo actual: ${cuenta.saldo}"
        else:
            return "Fondos insuficientes"

    def mostrar_saldo(self, cuenta):
        print(f"Cuenta {cuenta.numero} - Saldo: ${cuenta.saldo}")
