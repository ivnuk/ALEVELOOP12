import os
from unittest import TestCase

from pole_chudes.data_reader import CSVGetter

FILE_NAME = 'pole_chudes/words.csv'
TEST_FILE_NAME = 'test.csv'


class CSVGetterTest(TestCase):

    def setUp(self) -> None:
        self.data_reader = CSVGetter(FILE_NAME)

        with open(TEST_FILE_NAME, 'w') as fp:
            fp.write("""word\nproposal\ninsect\natmosphere\ncomputer\nrefrigerator""")
        pass

    def test_csv_getter_returns_a_word_as_string(self):
        word = self.data_reader.get_random_word()
        self.assertIsInstance(word, str)

    def test_csv_getter_returns_a_non_empty_string(self):
        word = self.data_reader.get_random_word()
        self.assertTrue(word)

    def test_csv_getter_does_not_return_same_word(self):
        with open(FILE_NAME) as fp:
            words = [x.strip('\n') for x in fp.readlines()][1:]
        removed_word = words.pop()
        word = self.data_reader.get_random_word(words)
        self.assertNotIn(word, words)
        self.assertEqual(removed_word, word)

    def tearDown(self) -> None:
        os.remove(TEST_FILE_NAME)
