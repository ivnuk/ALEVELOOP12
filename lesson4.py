class MyVerySpecialException(Exception):
    """
    Custom exception to manipulate user flow in the application.
    """


class ValidationError(Exception):
    """
    Exception raised in the case of invalid input.
    """

    def __init__(self, message, input_data):
        self.message = message
        self.input_data = input_data


class Rectangle:
    def __init__(self, width, height):
        if not isinstance(width, int) or \
                not isinstance(height, int):
            raise ValidationError('Width or height is not a number!:(', [width, height])
        if width < 0 or height < 0:
            raise ValidationError('Width and height must be positive numbers!', [width, height])
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def main():
    while True:
        try:
            width = int(input('enter width:'))
            height = int(input('enter height:'))
            rectangle = Rectangle(width, height)
        except ValueError as err:
            print(f'Cannot transform value to a number.')
        except ValidationError as err:
            print(err.message)
            print(f"{err.input_data} is not ok, bruh")
        else:
            print("Your rectangle square is ", rectangle.square())
            break
        finally:
            print("You've done it! Or not")


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        # todo
        pass

# alex@mail.com
# Alex@Mail.coM
# aLeX@mAiL.cOm
