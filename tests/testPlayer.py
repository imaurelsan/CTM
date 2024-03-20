import unittest
import sys
import json
import os
# Ajout du chemin du répertoire parent pour permettre l'importation des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.Player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Créer une instance de Player pour chaque test
        self.player = Player("John", "Doe", "1990-01-01", "123456")

    def test_init(self):
        # Vérifier si l'initialisation de l'objet Player fonctionne correctement
        self.assertEqual(self.player.first_name, "John")
        self.assertEqual(self.player.last_name, "Doe")
        self.assertEqual(self.player.birth_date, "1990-01-01")
        self.assertEqual(self.player.national_chess_id, "123456")

    def test_save_player(self):
        # Créer un joueur et vérifier s'il est correctement enregistré dans le fichier JSON
        self.player.save_player()
        self.assertTrue(os.path.exists('data/players.json'))
        with open('data/players.json', 'r') as file:
            players = json.load(file)
            self.assertEqual(len(players), 1)
            saved_player = players[0]
            self.assertEqual(saved_player['first_name'], self.player.first_name)
            self.assertEqual(saved_player['last_name'], self.player.last_name)
            self.assertEqual(saved_player['birth_date'], self.player.birth_date)
            self.assertEqual(saved_player['national_chess_id'], self.player.national_chess_id)

    def test_get_players(self):
        # Teste si la méthode get_players retourne correctement la liste des joueurs
        self.player.save_player()  # Enregistrer un joueur pour s'assurer qu'il existe dans le fichier JSON
        players = self.player.get_players()
        self.assertIsInstance(players, list)
        self.assertEqual(len(players), 1)
        retrieved_player = players[0]
        self.assertEqual(retrieved_player['first_name'], self.player.first_name)
        self.assertEqual(retrieved_player['last_name'], self.player.last_name)
        self.assertEqual(retrieved_player['birth_date'], self.player.birth_date)
        self.assertEqual(retrieved_player['national_chess_id'], self.player.national_chess_id)

    def tearDown(self):
        # Nettoyer les fichiers créés pendant les tests
        if os.path.exists('data/players.json'):
            os.remove('data/players.json')


if __name__ == '__main__':
    unittest.main()
