import unittest
from unittest.mock import patch
import sys
import os
# Ajoute le chemin du répertoire parent pour pouvoir importer les modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Views.MatchView import MatchView

class TestMatchView(unittest.TestCase):
    def setUp(self):
        self.match_view = MatchView()

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_valid(self, mock_input):
        # Teste si la méthode retourne le choix utilisateur valide
        user_choice = self.match_view.get_user_choice()
        self.assertEqual(user_choice, 1)

    @patch('builtins.input', side_effect=['2', 'invalid', '3'])
    def test_get_user_choice_invalid_then_valid(self, mock_input):
        # Teste si la méthode gère correctement une entrée utilisateur invalide puis valide
        user_choice = self.match_view.get_user_choice()
        self.assertEqual(user_choice, 2)

    @patch('builtins.input', side_effect=['invalid', '3'])
    def test_get_user_choice_invalid_then_valid_again(self, mock_input):
        # Teste si la méthode gère correctement une entrée utilisateur invalide suivie d'une entrée valide
        user_choice = self.match_view.get_user_choice()
        self.assertEqual(user_choice, 3)

    @patch('builtins.input', side_effect=['4', '2'])
    def test_get_user_choice_invalid_then_valid_with_multiple_attempts(self, mock_input):
        # Teste si la méthode gère correctement plusieurs entrées utilisateur invalides suivies d'une entrée valide
        user_choice = self.match_view.get_user_choice()
        self.assertEqual(user_choice, 2)

    @patch('builtins.input', side_effect=['a', '2'])
    def test_get_user_choice_invalid_then_valid_with_non_numeric_input(self, mock_input):
        # Teste si la méthode gère correctement une entrée non numérique suivie d'une entrée valide
        user_choice = self.match_view.get_user_choice()
        self.assertEqual(user_choice, 2)

    @patch('builtins.input', side_effect=['4', '5', '6', '2'])
    def test_get_user_choice_invalid_then_valid_with_multiple_invalid_inputs(self, mock_input):
        # Teste si la méthode gère correctement plusieurs entrées utilisateur invalides suivies d'une entrée valide
        user_choice = self.match_view.get_user_choice()
        self.assertEqual(user_choice, 2)

if __name__ == '__main__':
    unittest.main()
