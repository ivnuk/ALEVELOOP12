"""
системные библиотеки
import os
import uuid

сторонние библиотеки
import flask
import sqlalchemy

код, написанный нами в других файлах
from utils import something as sm


код, написанный нами
if __name__ == '__main__':
    pass
"""
I_AM_VERY_IMPORTANT_THING = False
DEBUG = True


class IAmVeryUsableAndFriendlyThing:
    pass


# wrong
class HttpConsumer:
    pass


# good
class SQLTransformer:
    pass


class A:
    pass


class B(A):
    pass


def func(x, y=None):
    pass


a = [x for x in range(1)]
b = lambda x: x ** 2

if __name__ == '__main__':
    a = 1 + 2 // 4 % 2
    b = 3 >= a > 0

    func(x=a, y=b)
    pass
    dct = {"a-level": 1,
           "b": 2, "c": 3,
           "d": 4, "e": 5}
    dct2 = dict(
        a=1,
        b=2,
        c=3)

# some_object.join().\
#             fitler().\
#             filter().\
#             all()
a = set()
b = set()
c = set()

# setting a as b union with c 
a = b.union(c)
