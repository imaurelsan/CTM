import unittest
from unittest.mock import patch  # Importation de patch depuis unittest.mock
import sys
import os
# Ajout du chemin du répertoire parent pour permettre l'importation des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Controllers.RoundsController import RoundsController

class TestRoundsController(unittest.TestCase):
    def setUp(self):
        self.rounds_controller = RoundsController()

    def test_shuffle_players_randomly(self):
        players = [{'first_name': 'John', 'last_name': 'Doe', 'score': 0},
                {'first_name': 'Jane', 'last_name': 'Doe', 'score': 0},
                {'first_name': 'Alice', 'last_name': 'Smith', 'score': 0},
                {'first_name': 'Bob', 'last_name': 'Smith', 'score': 0}]

        shuffled_players = self.rounds_controller.shuffle_players_randomly(players)

        self.assertEqual(len(shuffled_players), len(players))
        self.assertNotEqual(shuffled_players, players)
        # Vérifie si la liste a été mélangée en comparant les joueurs par leur nom complet
        self.assertNotEqual(shuffled_players[0]['first_name'] + ' ' + shuffled_players[0]['last_name'], players[0]['first_name'] + ' ' + players[0]['last_name'])
        self.assertNotEqual(shuffled_players[1]['first_name'] + ' ' + shuffled_players[1]['last_name'], players[1]['first_name'] + ' ' + players[1]['last_name'])


    def test_sort_players_by_score(self):
        players = [{'first_name': 'John', 'last_name': 'Doe', 'score': 2},
                   {'first_name': 'Jane', 'last_name': 'Doe', 'score': 1},
                   {'first_name': 'Alice', 'last_name': 'Smith', 'score': 2},
                   {'first_name': 'Bob', 'last_name': 'Smith', 'score': 1}]

        sorted_players = self.rounds_controller.sort_players_by_score(players)

        self.assertEqual(len(sorted_players), len(players))
        self.assertNotEqual(sorted_players, players)
        self.assertEqual(sorted_players[0]['score'], 2)

    @patch('builtins.input', side_effect=[1])
    def test_get_match_results(self, mock_input):
        matches = [{'player1': {'first_name': 'John', 'last_name': 'Doe'},
                    'player2': {'first_name': 'Jane', 'last_name': 'Doe'}}]
        current_round = 1

        match_results = self.rounds_controller.get_match_results(matches, current_round)

        self.assertEqual(len(match_results), 1)
        self.assertEqual(match_results[0][0][0], 'John Doe')

    # Add more tests for other methods as needed

if __name__ == '__main__':
    unittest.main()
