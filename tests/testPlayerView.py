import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Ajoute le chemin du répertoire parent pour importer les modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Views.PlayerView import PlayerView

class TestPlayerView(unittest.TestCase):

    # Test de la méthode get_player_info
    @patch('builtins.input', side_effect=['John', 'Doe', '01/01/1990', 'AB12345'])
    def test_get_player_info(self, mock_input):
        player_view = PlayerView()
        first_name, last_name, birth_date, national_chess_id = player_view.get_player_info()

        self.assertEqual(first_name, 'John')
        self.assertEqual(last_name, 'Doe')
        self.assertEqual(birth_date, '01/01/1990')
        self.assertEqual(national_chess_id, 'AB12345')

    # Test de la méthode select_player
    @patch('builtins.input', return_value='2')
    def test_select_player(self, mock_input):
        player_view = PlayerView()
        players = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '01/01/1990', 'national_chess_id': 'AB12345'},
                   {'first_name': 'Jane', 'last_name': 'Smith', 'birth_date': '02/02/1991', 'national_chess_id': 'CD67890'}]
        
        # Rediriger stdout pour capturer l'affichage
        captured_output = StringIO()
        sys.stdout = captured_output

        selected_index = player_view.select_player(players)

        # Rétablir stdout
        sys.stdout = sys.__stdout__

        # Vérifier la sortie standard
        self.assertIn('1 - John Doe - Né le 01/01/1990 - ID: AB12345', captured_output.getvalue())
        self.assertIn('2 - Jane Smith - Né le 02/02/1991 - ID: CD67890', captured_output.getvalue())

        # Vérifier l'indice sélectionné
        self.assertEqual(selected_index, 1)  # Index 1 car l'entrée utilisateur est "2" et l'indice est inversé

if __name__ == '__main__':
    unittest.main()
