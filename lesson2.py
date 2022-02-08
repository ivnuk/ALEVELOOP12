"""
OOP Lesson 2.
- super, __init__, __new__.
- "Dunder" methods.
"""

"""
How the web app works:
User with mouse (computer mouse):
http(s) get request -> web server (nginx, apache) -> django app 
django app -> (middleware might change request) view (might change response also) -> return response (html) -> user see your homepage
"""

# import sys, os -> don't do that

import os
import sys

from datetime import datetime, date, timedelta

# import datetime as dt


class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self, direction):
        return f"I'm moving to the {direction}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    # def __getattribute__(self, item):
    #     if item == 'name':
    #         raise AttributeError('You can\'t know the name')
    #     return super().__getattribute__(item)

    def __getattr__(self, item):
        return item


class Child(Parent):

    @classmethod
    def __new__(cls, *args, **kw):
        print(kw)
        return super().__new__(cls)

    def __init__(self, unique_id, *args, **kwargs):
        self.init_time = datetime.now()
        self.unique_id = unique_id
        super().__init__(*args, **kwargs)
        print('Init time:', self.init_time)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name} | {self.unique_id}'

    def __del__(self):
        # self.conn.close() ! do that
        # del self ! don't do that
        # garb col -> obj -> del obj -> __del__ -> del obj -> __del__ -> ...
        # logger.log(some info)
        print(f'{self.name} | Destroy time:', datetime.now())

    def __call__(self, x, y):
        # calculate numbers
        return x + y

    def move(self, direction):
        # write to logs
        return super().move(direction) + ', but slowly :('


if __name__ == '__main__':
    child_1 = Child(unique_id=12345, **{"name": 'Ivan', "age": 1})  # Child.__new__(**params).__init(**params)
    child_2 = Child(unique_id=42, name='Anton', age=15)
    # print(child_1.name, child_1.age, child_1.unique_id)

    # move('kitchen') -> I'm moving to the kitchen
    # move('kitchen') -> I'm moving to the kitchen, but slowly :(

    # print(child_1.move('bathroom'))
    del child_1
    # sleep(5)
    # print(child_2)
    # print(child_2(12, 7))
    parent_1 = Parent('Grisha', 25)
    parent_2 = Parent('Oleg', 34)

    # print(parent_1 < parent_2)
    # print(parent_1 <= parent_2)
    # print(parent_1 > parent_2)
    # print(parent_1 >= parent_2)
    # print(parent_1 == parent_2)
    # print(parent_1 != parent_2)

    # print(parent_1.unique_id)
    # print(parent_1.unique_id)
    # print(hasattr(parent_1, 'unique_id'))
    # print(hasattr(parent_1, 'move'))
    # print(getattr(parent_1, 'unique_id', f'{parent_1.name} {parent_1.age}'))
    # print(setattr(parent_1, 'unique_id', 505))
    # print(parent_1.unique_id)

    some_dict = {'a': 1, 'b': 2}
    print(some_dict.get('c', 42))
    print(some_dict)

    a = [x for x in range(100000)]  # iterator
    b = (x for x in range(100000))  # generator
