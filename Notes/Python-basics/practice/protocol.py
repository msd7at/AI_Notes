from typing import Protocol
class Animal(Protocol):

    def speak(self) -> str:
        ...
    def eat(self) -> str:
        ...



