# Solución al ejercicio SRP

class UserManager:
    def add_user(self, user):
        print(f"Usuario {user} agregado")

class UserNotifier:
    def notify_user(self, user):
        print(f"Notificando a {user}")

if __name__ == "__main__":
    user_manager = UserManager()
    notifier = UserNotifier()
    user = "Juan"
    user_manager.add_user(user)
    notifier.notify_user(user)