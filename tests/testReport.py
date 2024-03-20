import unittest
from unittest.mock import patch
import os
import sys
import json
# Ajout du chemin du répertoire parent pour permettre l'importation des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.Report import Report


class TestReport(unittest.TestCase):
    def setUp(self):
        self.report = Report()

    def test_load_players_success(self):
        # Création temporaire d'un fichier players.json valide
        with open('data/players.json', 'w') as file:
            json.dump([{'name': 'John'}, {'name': 'Jane'}], file)

        players = self.report.load_players()
        self.assertEqual(len(players), 2)

        # Suppression du fichier temporaire
        os.remove('data/players.json')

    @patch('builtins.print')
    def test_load_players_file_not_found(self, mock_print):
        players = self.report.load_players()
        self.assertEqual(players, [])
        mock_print.assert_called_with("Le fichier des joueurs n'existe pas.")

    @patch('builtins.print')
    def test_load_players_json_error(self, mock_print):
        # Création temporaire d'un fichier players.json invalide
        with open('data/players.json', 'w') as file:
            file.write("Invalid JSON")

        players = self.report.load_players()
        self.assertEqual(players, [])
        mock_print.assert_called_with("Erreur lors de la lecture du fichier JSON.")

        # Suppression du fichier temporaire
        os.remove('data/players.json')

    def test_load_tournaments_success(self):
        # Création temporaire d'un fichier tournaments.json valide
        with open('data/tournaments.json', 'w') as file:
            json.dump([{'name': 'Tournament 1'}, {'name': 'Tournament 2'}], file)

        tournaments = self.report.load_tournaments()
        self.assertEqual(len(tournaments), 2)

        # Suppression du fichier temporaire
        os.remove('data/tournaments.json')

    @patch('builtins.print')
    def test_load_tournaments_file_not_found(self, mock_print):
        tournaments = self.report.load_tournaments()
        self.assertEqual(tournaments, [])
        mock_print.assert_called_with("Le fichier des tournois n'existe pas.")

    @patch('builtins.print')
    def test_load_tournaments_json_error(self, mock_print):
        # Création temporaire d'un fichier tournaments.json invalide
        with open('data/tournaments.json', 'w') as file:
            file.write("Invalid JSON")

        tournaments = self.report.load_tournaments()
        self.assertEqual(tournaments, [])
        mock_print.assert_called_with("Erreur lors de la lecture du fichier JSON.")

        # Suppression du fichier temporaire
        os.remove('data/tournaments.json')

if __name__ == '__main__':
    unittest.main()
