class Employee:
    def work(self):
        return 'I come to the office'


class Programmer(Employee):
    def work(self):
        """
        call super and add extra symbols
        """