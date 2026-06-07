from interfaces import Observer


class NotificationService(Observer):
    def __init__(self):
        self.smtp_server = "smtp.library.local"

    def update(self, book_title: str) -> None:
        print(
            f"[Email Service] Відправка email: "
            f"'Нове надходження: {book_title}' через {self.smtp_server}"
        )
