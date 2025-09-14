# Solución al ejercicio OCP

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Procesando pago con tarjeta: {amount}")

class PaypalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Procesando pago con PayPal: {amount}")

# Nuevo método de pago agregado sin modificar clases existentes
class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Procesando pago con Criptomoneda: {amount}")

class PaymentProcessor:
    def process(self, payment_method: PaymentMethod, amount):
        payment_method.pay(amount)

if __name__ == "__main__":
    processor = PaymentProcessor()
    processor.process(CreditCardPayment(), 100)
    processor.process(PaypalPayment(), 50)
    processor.process(CryptoPayment(), 200)