import unittest
import sys
import os
# Ajout du chemin du répertoire parent pour permettre l'importation des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.Match import Match  # Importation de la classe Match depuis le module Models
from Controllers.MatchController import MatchController  # Importation de la classe MatchController


class TestMatchController(unittest.TestCase):
    def setUp(self):
        """
        Configuration initiale pour chaque test.
        """
        self.match_controller = MatchController()  # Création d'une instance de MatchController pour chaque test

    def test_create_matches(self):
        """
        Teste la fonction create_matches du MatchController.
        """
        # Création de joueurs factices
        players = [{'first_name': 'player1', 'last_name': 'A'},
                   {'first_name': 'player2', 'last_name': 'B'},
                   {'first_name': 'player3', 'last_name': 'C'},
                   {'first_name': 'player4', 'last_name': 'D'}]

        # Création de paires de joueurs
        pairs = [(players[0], players[1]), (players[2], players[3])]

        # Appel de la fonction à tester
        matches = self.match_controller.create_matches(pairs)

        # Vérifications des résultats
        self.assertEqual(len(matches), 2)  # Vérifie si deux matches ont été créés
        self.assertIsInstance(matches[0], Match)  # Vérifie si le premier élément est une instance de Match
        self.assertIsInstance(matches[1], Match)  # Vérifie si le deuxième élément est une instance de Match

    def test_pair_players(self):
        """
        Teste la fonction pair_players du MatchController.
        """
        # Joueurs triés et matches joués précédemment
        sorted_players = [{'first_name': 'player1', 'last_name': 'A'},
                          {'first_name': 'player2', 'last_name': 'B'},
                          {'first_name': 'player3', 'last_name': 'C'},
                          {'first_name': 'player4', 'last_name': 'D'}]
        played_matches = [Match(sorted_players[0], sorted_players[1]),
                          Match(sorted_players[2], sorted_players[3])]

        # Appel de la fonction à tester
        paired_players = self.match_controller.pair_players(sorted_players, played_matches)

        # Vérification des résultats
        self.assertEqual(len(paired_players), 2)  # Vérifie si deux paires de joueurs ont été appariées

    def test_has_played_together(self):
        """
        Teste la fonction has_played_together du MatchController.
        """
        # Joueurs et matches joués précédemment
        player1 = {'first_name': 'player1', 'last_name': 'A'}
        player2 = {'first_name': 'player2', 'last_name': 'B'}
        played_matches = [Match(player1, player2)]

        # Vérifie si les joueurs ont joué ensemble
        self.assertTrue(self.match_controller.has_played_together(player1, player2, played_matches))

        # Vérifie si les joueurs n'ont pas joué ensemble
        self.assertFalse(self.match_controller.has_played_together(player1, {'first_name': 'player3', 'last_name': 'C'}, played_matches))
        self.assertFalse(self.match_controller.has_played_together(player1, {'first_name': 'player4', 'last_name': 'D'}, played_matches))


if __name__ == '__main__':
    unittest.main()  # Exécute les tests si le script est exécuté en tant que programme principal
