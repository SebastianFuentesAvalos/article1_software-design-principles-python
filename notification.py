from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailSender(NotificationSender):
    def send(self, message):
        print(f"Sending EMAIL: {message}")

class SMSSender(NotificationSender):
    def send(self, message):
        print(f"Sending SMS: {message}")

def notify(sender: NotificationSender, message: str):
    sender.send(message)

if __name__ == "__main__":
    email_sender = EmailSender()
    sms_sender = SMSSender()
    notify(email_sender, "Hello via Email!")
    notify(sms_sender, "Hello via SMS!")