import unittest
from secretary_program import get_doc_owner_name, delete_doc, add_new_doc


documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]


class TestFunctionSecretary_program(unittest.TestCase):

    def test_get_doc_owner_name(self):
        self.assertEqual('Аристарх Павлов', get_doc_owner_name('10006'), 'Запись не найдена')

    def test_delete_doc(self):
        self.assertEqual(('11-2', True), delete_doc('11-2'), 'Указанного документа нет')

    def test_add_new_doc(self):
        self.assertEqual('4', add_new_doc('111', 'pasport', 'Ivan Ivanov', '4'), 'Документ не создан')


if __name__ == '__main__':
    unittest.main()
