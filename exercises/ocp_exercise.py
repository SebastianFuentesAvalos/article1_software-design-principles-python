"""
Ejercicio OCP: Refactoriza para que puedas agregar nuevos métodos de pago sin modificar la clase 'PaymentProcessor'.

class PaymentProcessor:
    def process(self, payment_type, amount):
        if payment_type == "credit_card":
            print(f"Procesando pago con tarjeta: {amount}")
        elif payment_type == "paypal":
            print(f"Procesando pago con PayPal: {amount}")

# Tu tarea:
# 1. Refactoriza usando herencia y polimorfismo (Open/Closed Principle).
# 2. Demuestra cómo agregar un nuevo método de pago.
"""