import csv
import uuid
from functools import wraps

NO_ARGS_UUIDS = ['uuid1', 'uuid4']
ARGS_UUIDS = ('uuid3', 'uuid5')
NAMESPACE = 'a-level'


def deco_with_parameters(arg_1, arg_2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(arg_1, arg_2)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def deco(func):
    # must have
    @wraps(func)
    def wrapper(*args, **kwargs):
        # must call
        id_type = args[0] if len(args) > 0 else list(kwargs.values())[0]
        # do things before call
        if id_type in NO_ARGS_UUIDS:
            result = func(id_type)
        elif id_type in ARGS_UUIDS:
            result = func(id_type,
                          uuid.NAMESPACE_X500,
                          __name__)
        else:
            raise ValueError('invalid uuid type')
        result = str(result).replace('-', '').upper()
        # must return
        return result
    # always return w/o parentheses
    return wrapper


@deco
def generate_uid(id_type: str, namespace=None, name=None):
    if namespace and name:
        return getattr(uuid, id_type)(namespace=namespace, name=name)
    return getattr(uuid, id_type)()


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f"{self.last_name} {self.first_name} | {self.age}"

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @staticmethod
    def some_static_method():
        return 'I am static'

    @classmethod
    def from_csv(cls, file_path):
        with open(file_path) as fp:
            reader = csv.DictReader(fp)
            return [cls(**dict(data)) for data in reader]


if __name__ == '__main__':
    # id_ = generate_uid('uuid4')
    # print(id_)
    # print(type(id_))
    # me = Person('Ihor', 'Vnukov', 31)
    # print(me.full_name)
    # print(me.some_static_method())
    # print(Person.some_static_method())
    # print(Person.from_csv('persons.csv'))
    print(generate_uid)
