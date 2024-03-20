import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Ajouter le chemin du répertoire parent pour importer les modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Views.ReportView import ReportView

class TestReportView(unittest.TestCase):

    # Test de la méthode display_players_alphabetical
    def test_display_players_alphabetical(self):
        report_view = ReportView()
        players = [{'first_name': 'John', 'last_name': 'Doe', 'national_chess_id': 'AB12345'},
                   {'first_name': 'Jane', 'last_name': 'Smith', 'national_chess_id': 'CD67890'}]
        
        # Rediriger stdout pour capturer l'affichage
        captured_output = StringIO()
        sys.stdout = captured_output

        report_view.display_players_alphabetical(players)

        # Rétablir stdout
        sys.stdout = sys.__stdout__

        # Vérifier la sortie standard
        expected_output = "\nListe des joueurs par ordre alphabétique:\nDoe John (INE: AB12345)\nSmith Jane (INE: CD67890)\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    # Test de la méthode display_tournaments
    def test_display_tournaments(self):
        report_view = ReportView()
        tournaments = [{'name': 'Tournament 1'}, {'name': 'Tournament 2'}]
        
        # Rediriger stdout pour capturer l'affichage
        captured_output = StringIO()
        sys.stdout = captured_output

        report_view.display_tournaments(tournaments)

        # Rétablir stdout
        sys.stdout = sys.__stdout__

        # Vérifier la sortie standard
        expected_output = "\nListe de tous les tournois :\nTournament 1\nTournament 2\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    # Test de la méthode display_tournament_infos
    def test_display_tournament_infos(self):
        report_view = ReportView()
        tournament = {'name': 'Tournament 1', 'location': 'Location 1', 'start_date': '01/01/2024', 'end_date': '02/01/2024'}
        
        # Rediriger stdout pour capturer l'affichage
        captured_output = StringIO()
        sys.stdout = captured_output

        report_view.display_tournament_infos(tournament)

        # Rétablir stdout
        sys.stdout = sys.__stdout__

        # Vérifier la sortie standard
        expected_output = "\nDétails du tournoi :\nNom: Tournament 1\nLieu: Location 1\nDate de début: 01/01/2024\nDate de fin: 02/01/2024\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    # Ajoutez d'autres tests pour les autres méthodes de la classe ReportView

if __name__ == '__main__':
    unittest.main()
