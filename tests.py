from unittest import TestCase

from lesson4 import Rectangle


class RectangleTest(TestCase):
    def test_square(self):
        rectangle = Rectangle(2, 8)
        square = rectangle.square()
        self.assertEqual(16, square)

    def test_perimeter(self):
        rectangle = Rectangle(3, 5)
        perimeter = rectangle.perimeter()
        self.assertEquals(16, perimeter)

