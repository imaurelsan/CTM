import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Ajouter le chemin du répertoire parent pour importer les modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Views.RoundsView import RoundsView

class TestRoundsView(unittest.TestCase):

    # Test de la méthode ask_for_next_round
    @patch('builtins.input', return_value='o')
    def test_ask_for_next_round_yes(self, mock_input):
        rounds_view = RoundsView()
        user_response = rounds_view.ask_for_next_round()
        self.assertEqual(user_response, 'o')

    @patch('builtins.input', return_value='n')
    def test_ask_for_next_round_no(self, mock_input):
        rounds_view = RoundsView()
        user_response = rounds_view.ask_for_next_round()
        self.assertEqual(user_response, 'n')

if __name__ == '__main__':
    unittest.main()
