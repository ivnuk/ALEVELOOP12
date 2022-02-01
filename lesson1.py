# Продуктовый магазин
# Продукты питания + бытовая химия


class Good:
    def __init__(self, price, amount, category='food'):
        self.price = price
        self.amount = amount
        self.category = category

    def __total(self):
        return self.price * self.amount

    def get_total(self):
        return self.__total()


class Purchase:

    def subtotal(self, list_of_products):
        return sum([x.total() for x in list_of_products])

    # def subtotal(self, list_of_products, discount):
    #     pass


class SomeAnotherClass:
    def subtotal(self):
        pass


class Human:
    def __init__(self, name, sex, race):
        self.name = name
        self.sex = sex
        self.race = race

    def walk(self):
        print('I am walking')

    def say_hello(self):
        print(f'Hi, my name is {self.name}')


class Parent(Human):
    def work(self):
        print('I\'m working!')


class Child(Parent):
    def work(self):
        raise Exception('It\'s illegal')

    def say_hello(self):
        print(f'Sup! I\'m {self.name}')


def subttl():
    print('hello')


if __name__ == '__main__':
    grecha = Good(price=50, amount=1)
    apples = Good(25, 1.7)
    # butter = Good()
    # print(butter.amount)
    # Good.amount = 3
    # print(butter.amount)
    # bread = Good()
    # print('maslo:', butter.get_total())
    # print('grecha:', grecha.__total())
    # print('apples:', apples._total())
    # print(Purchase().subtotal([grecha, apples]))
    purchase = Purchase()
    purchase.id_ = '1123456789'
    print(purchase.id_)
    purchase2 = Purchase()
    # print(purchase2.id_)
    purchase2.subtotal = subttl
    print(purchase2.subtotal())
    del purchase2.subtotal
    purchase2.subtotal()
