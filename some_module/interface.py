from abc import ABC, abstractmethod


# Это абстрактный класс. Абстрактный, потому, что ничего не делает, только задает набор функций и их сигнатуры.
class SomeInterface(ABC):

    @abstractmethod
    def func1(self, a, b, c):
        pass

    @abstractmethod
    def func2(self, x, y):
        pass