"""
Ejercicio SRP: Refactoriza la clase 'UserManager' para que cumpla el principio de responsabilidad única (SRP).
Actualmente maneja usuarios y también los notifica. Divide las responsabilidades.

class UserManager:
    def add_user(self, user):
        print(f"Usuario {user} agregado")
        self.notify_user(user)

    def notify_user(self, user):
        print(f"Notificando a {user}")

# Tu tarea:
# 1. Refactoriza el código para que 'UserManager' solo agregue usuarios.
# 2. Crea una nueva clase que se encargue de las notificaciones.
# 3. Demuestra cómo se usarían ambas clases juntas.
"""