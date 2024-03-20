import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Ajoute le chemin du répertoire parent pour importer les modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Views.TournamentView import TournamentView

class TestTournamentView(unittest.TestCase):

    # Test de la méthode get_tournament_info
    @patch('builtins.input', side_effect=['Chess Tournament', 'New York', '01/01/2024', '02/01/2024', '5', 'A grand chess event'])
    def test_get_tournament_info(self, mock_input):
        tournament_view = TournamentView()
        name, location, start_date, end_date, rounds, description = tournament_view.get_tournament_info()

        self.assertEqual(name, 'Chess Tournament')
        self.assertEqual(location, 'New York')
        self.assertEqual(start_date, '01/01/2024')
        self.assertEqual(end_date, '02/01/2024')
        self.assertEqual(rounds, 5)
        self.assertEqual(description, 'A grand chess event')

    # Test de la méthode select_tournament
    @patch('builtins.input', return_value='2')
    def test_select_tournament(self, mock_input):
        tournament_view = TournamentView()
        tournaments = [
            {'id': 1, 'name': 'Tournament A', 'location': 'Paris', 'start_date': '01/01/2024', 'end_date': '02/01/2024', 'rounds': 4, 'player_list': []},
            {'id': 2, 'name': 'Tournament B', 'location': 'New York', 'start_date': '03/01/2024', 'end_date': '04/01/2024', 'rounds': 5, 'player_list': []}
        ]

        # Rediriger stdout pour capturer l'affichage
        captured_output = StringIO()
        sys.stdout = captured_output

        selected_id = tournament_view.select_tournament(tournaments)

        # Rétablir stdout
        sys.stdout = sys.__stdout__

        # Vérifier la sortie standard
        self.assertIn('1 - Tournament A à Paris du 01/01/2024 au 02/01/2024 - Rounds: 4 - Inscrits: 0', captured_output.getvalue())
        self.assertIn('2 - Tournament B à New York du 03/01/2024 au 04/01/2024 - Rounds: 5 - Inscrits: 0', captured_output.getvalue())

        # Vérifier l'ID sélectionné
        self.assertEqual(selected_id, 1)  # ID 1 car l'entrée utilisateur est "2" et l'indice est inversé

if __name__ == '__main__':
    unittest.main()
