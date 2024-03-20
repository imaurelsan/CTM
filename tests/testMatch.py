import unittest
import sys
import os
# Ajout du chemin du répertoire parent pour permettre l'importation des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.Match import Match

class TestMatch(unittest.TestCase):
    def setUp(self):
        # Initialisation de deux joueurs fictifs pour les tests
        self.player1 = {'first_name': 'John', 'last_name': 'Doe'}
        self.player2 = {'first_name': 'Jane', 'last_name': 'Smith'}

        # Création d'un match pour les tests
        self.match = Match(self.player1, self.player2)

    def test_init(self):
        # Vérifier si les joueurs sont correctement attribués lors de l'initialisation
        self.assertEqual(self.match.player1, self.player1)
        self.assertEqual(self.match.player2, self.player2)
        # Vérifier si le vainqueur est initialisé à None
        self.assertIsNone(self.match.winner)

    def test_serialize(self):
        # Vérifier si la méthode serialize renvoie un dictionnaire avec les bonnes clés et valeurs
        serialized_match = self.match.serialize()
        self.assertIsInstance(serialized_match, dict)
        self.assertEqual(serialized_match['player1'], self.player1)
        self.assertEqual(serialized_match['player2'], self.player2)
        self.assertIsNone(serialized_match['winner'])

    def test_str(self):
        # Vérifier si la méthode str renvoie une chaîne de caractères correcte représentant le match
        expected_str = f"{self.player1['first_name']} {self.player1['last_name']} VS {self.player2['first_name']} {self.player2['last_name']}"
        self.assertEqual(str(self.match), expected_str)

if __name__ == '__main__':
    unittest.main()
