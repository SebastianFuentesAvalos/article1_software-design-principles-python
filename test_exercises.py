# Test básico para verificar las soluciones de los ejercicios.

def test_srp_solution():
    try:
        from solutions.srp_solution import UserManager, UserNotifier
        user_manager = UserManager()
        notifier = UserNotifier()
        user_manager.add_user("TestUser")
        notifier.notify_user("TestUser")
        print("SRP Solution: OK")
    except Exception as e:
        print(f"SRP Solution: ERROR - {e}")

def test_ocp_solution():
    try:
        from solutions.ocp_solution import PaymentProcessor, CreditCardPayment, PaypalPayment, CryptoPayment
        processor = PaymentProcessor()
        processor.process(CreditCardPayment(), 10)
        processor.process(PaypalPayment(), 20)
        processor.process(CryptoPayment(), 30)
        print("OCP Solution: OK")
    except Exception as e:
        print(f"OCP Solution: ERROR - {e}")

if __name__ == "__main__":
    test_srp_solution()
    test_ocp_solution()