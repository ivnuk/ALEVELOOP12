class Employee:
    a = 1

    def __init__(self, a):
        self.a = a

    def work(self):
        return 'I come to the office'


class Programmer(Employee):
    def work(self):
        """
        call super and add extra symbols
        """

    def _secret_method(self):
        pass

    def another_method(self):
        self._secret_method()


def func():
    pass


prog1 = Programmer()

prog1._secret_method()
