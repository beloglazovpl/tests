import unittest
from yandexapi import check_folder, create_folder


class TestYandexAPI(unittest.TestCase):

    def test_create_folder(self):
        self.assertEqual(201, create_folder('test_folder'), 'Папка не создана')

    def test_check_folder(self):
        self.assertEqual(200, check_folder('test_folder'), 'Данной папки нет')



if __name__ == '__main__':
    unittest.main()
