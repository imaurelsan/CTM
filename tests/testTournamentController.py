import unittest
from unittest.mock import patch
import sys
import os

# Ajout du chemin du répertoire parent pour que le test puisse importer le module TournamentController
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import de la classe TournamentController à tester
from Controllers.TournamentController import TournamentController


class TestTournamentController(unittest.TestCase):
    def setUp(self):
        self.controller = TournamentController()

    # Test de la création de tournoi
    @patch('Views.TournamentView.TournamentView.get_tournament_info',
           return_value=('Tournament', 'Location', '2024-01-01', '2024-01-05', 3, 'Description'))
    def test_create_tournament(self, mock_get_tournament_info):
        self.controller.create_tournament()
        # On s'attend à ce que le tournoi soit créé avec les informations fournies
        self.assertIsNotNone(self.controller.tournament.name)
        self.assertIsNotNone(self.controller.tournament.location)
        self.assertIsNotNone(self.controller.tournament.start_date)
        self.assertIsNotNone(self.controller.tournament.end_date)
        self.assertIsNotNone(self.controller.tournament.rounds)
        self.assertIsNotNone(self.controller.tournament.description)

    # Test de l'ajout de joueur à un tournoi
    @patch('Views.PlayerView.PlayerView.select_player', return_value=0)
    @patch('Views.TournamentView.TournamentView.select_tournament', return_value=1)
    def test_add_player_to_tournament(self, mock_select_tournament, mock_select_player):
        # Configuration des données d'entrée
        self.controller.tournament.get_tournaments = lambda: [{'id': 1, 'rounds': 3, 'player_list': []}]
        self.controller.player.get_players = lambda: [{'id': 1, 'name': 'Player1'}]

        # Ajout d'un joueur à un tournoi vide
        self.controller.add_player_to_tournament()
        # On s'attend à ce que le joueur soit ajouté au tournoi
        self.assertEqual(len(self.controller.tournament.tournaments[0]['player_list']), 1)

        # Ajout d'un joueur à un tournoi plein
        self.controller.add_player_to_tournament()
        # On s'attend à ce que le joueur ne soit pas ajouté au tournoi plein
        self.assertEqual(len(self.controller.tournament.tournaments[0]['player_list']), 1)

    # Test de l'ajout d'un joueur à un tournoi complet
    @patch('Views.PlayerView.PlayerView.select_player', return_value=0)
    @patch('Views.TournamentView.TournamentView.select_tournament', return_value=1)
    def test_add_player_to_full_tournament(self, mock_select_tournament, mock_select_player):
        # Configuration des données d'entrée
        self.controller.tournament.get_tournaments = lambda: [{'id': 1, 'rounds': 1, 'player_list': [{'id': 2}]}]
        self.controller.player.get_players = lambda: [{'id': 1, 'name': 'Player1'}]

        # Ajout d'un joueur à un tournoi plein
        self.controller.add_player_to_tournament()
        # On s'attend à ce que le joueur ne soit pas ajouté au tournoi plein
        self.assertEqual(len(self.controller.tournament.tournaments[0]['player_list']), 1)


if __name__ == '__main__':
    unittest.main()
