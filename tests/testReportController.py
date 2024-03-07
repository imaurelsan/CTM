import unittest
from unittest.mock import patch  # Importation de patch depuis unittest.mock
import sys
import os
# Ajout du chemin du répertoire parent pour permettre l'importation des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Controllers.ReportController import ReportController

class TestReportController(unittest.TestCase):
    @patch.object(ReportController, 'list_tournaments', return_value=[{"name": "Tournament 1", "id": 1, "player_list": []}])
    def test_list_tournaments(self, mock_list_tournaments):
        controller = ReportController()
        tournaments = controller.list_tournaments()
        self.assertEqual(len(tournaments), 1)
        self.assertEqual(tournaments[0]['name'], "Tournament 1")
        mock_list_tournaments.assert_called_once()

    def test_players_alphabetical(self):
        controller = ReportController()
        sorted_players = controller.players_alphabetical()
        # En supposant qu'on a  quelques joueurs d'exemple dans la classe Report
        self.assertEqual(sorted_players[0]['last_name'], "Doe")
        self.assertEqual(sorted_players[0]['first_name'], "John")

    def test_list_tournaments(self):
        controller = ReportController()
        tournaments = controller.list_tournaments()
        # En supposant qu'on a  quelques tournois d'exemple dans la classe Report
        self.assertEqual(len(tournaments), 3)
        self.assertEqual(tournaments[0]['name'], "Tournament 1")

    @patch('builtins.input', side_effect=['1'])  # Simuler l'entrée utilisateur
    def test_tournament_players_alphabetical(self, mock_input):
        controller = ReportController()
        sorted_players = controller.tournament_players_alphabetical()
        # En supposant qu'on a  quelques joueurs d'exemple dans la liste de joueurs du tournoi
        self.assertEqual(sorted_players[0]['last_name'], "Doe")
        self.assertEqual(sorted_players[0]['first_name'], "Jane")

    @patch('Controllers.ReportController.Report.load_tournaments', return_value=[{"name": "Tournament 1", "round_list": [], "id": 1, "player_list": [{"last_name": "Doe", "first_name": "John", "score": 100}] }])
    def test_get_tournament_rounds_and_matches(self, mock_load_tournaments):
        controller = ReportController()
        tournament_name, rounds, tournament_id = controller.get_tournament_rounds_and_matches()
        self.assertEqual(tournament_name, "Tournament 1")
        self.assertEqual(len(rounds), 0)
        self.assertEqual(tournament_id, 1)

    @patch('Controllers.ReportController.Report.load_tournaments', return_value=[{"name": "Tournament 1", "id": 1, "player_list": [{"last_name": "Doe", "first_name": "John", "score": 100}] }])
    def test_get_tournament_players_sorted(self, mock_load_tournaments):
        controller = ReportController()
        sorted_players = controller.get_tournament_players_sorted(1)
        # En supposant qu'on a quelques joueurs d'exemple dans la liste de joueurs du tournoi
        self.assertEqual(sorted_players[0]['last_name'], "Doe")
        self.assertEqual(sorted_players[0]['first_name'], "John")
        self.assertEqual(sorted_players[0]['score'], 100)


if __name__ == '__main__':
    unittest.main()
