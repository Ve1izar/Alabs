from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, book_title: str) -> None:
        pass

# Інтерфейс для суб'єкта (видавця подій)
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, book_title: str) -> None:
        pass
