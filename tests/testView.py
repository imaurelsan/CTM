import unittest
from Views.View import View

class TestView(unittest.TestCase):

    def setUp(self):
        self.view = View()

    def test_is_valid_date(self):
        self.assertTrue(self.view.is_valid_date("01/01/2022"))
        self.assertFalse(self.view.is_valid_date("2022/01/01"))
        self.assertFalse(self.view.is_valid_date("32/01/2022"))
        self.assertFalse(self.view.is_valid_date("01/13/2022"))
        self.assertFalse(self.view.is_valid_date("01/01/22"))
        self.assertFalse(self.view.is_valid_date("01-01-2022"))

    def test_is_valid_id(self):
        self.assertTrue(self.view.is_valid_id("AB12345"))
        self.assertTrue(self.view.is_valid_id("ab12345"))
        self.assertFalse(self.view.is_valid_id("12345AB"))
        self.assertFalse(self.view.is_valid_id("ABCD12345"))

    def test_is_valid_alpha(self):
        self.assertTrue(self.view.is_valid_alpha("John Doe"))
        self.assertTrue(self.view.is_valid_alpha("John-Doe"))
        self.assertTrue(self.view.is_valid_alpha("Jøhn"))
        self.assertFalse(self.view.is_valid_alpha("123"))
        self.assertFalse(self.view.is_valid_alpha("J"))

    def test_is_valid_int(self):
        self.assertTrue(self.view.is_valid_int("123"))
        self.assertTrue(self.view.is_valid_int("0"))
        self.assertFalse(self.view.is_valid_int("123.45"))
        self.assertFalse(self.view.is_valid_int("abc"))

    # Test de la méthode get_valid_date_input
    def test_get_valid_date_input(self):
        # Simuler une saisie utilisateur
        with unittest.mock.patch('builtins.input', return_value='01/01/2022'):
            date = self.view.get_valid_date_input("Entrez une date : ")
            self.assertEqual(date, "01/01/2022")

    # Test de la méthode get_valid_alpha_input
    def test_get_valid_alpha_input(self):
        # Simuler une saisie utilisateur
        with unittest.mock.patch('builtins.input', return_value='John Doe'):
            alpha_string = self.view.get_valid_alpha_input("Entrez un nom : ")
            self.assertEqual(alpha_string, "John Doe")

    # Test de la méthode get_valid_int_input
    def test_get_valid_int_input(self):
        # Simuler une saisie utilisateur
        with unittest.mock.patch('builtins.input', return_value='123'):
            integer = self.view.get_valid_int_input("Entrez un entier : ")
            self.assertEqual(integer, 123)

if __name__ == '__main__':
    unittest.main()
