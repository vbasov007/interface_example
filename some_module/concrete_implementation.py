from .interface import SomeInterface


# Это конкретная реализация интерфейса, заданного классом SomeInterface. Если ты не создашь реализацию всех функций,
# которые заданы в SomeInterface, то это здесь покажется как предупреждение.
# Python не следит за этим строго и даже если ты не опишешь все функции, скрипт все равно запустится, но будет выдавать
# предупреждения.
class ConcreteImplementation(SomeInterface):

    def __init__(self):
        print('This is initialization')

    def func1(self, a, b, c):
        print(a + b + c)

    def func2(self, x, y):
        print(x*y)

