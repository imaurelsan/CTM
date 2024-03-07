import unittest
import sys
import os
# Ajout du chemin du répertoire parent pour permettre l'importation des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.Player import Player
from Views.PlayerView import PlayerView
from Controllers.PlayerController import PlayerController


class TestPlayerController(unittest.TestCase):
    def setUp(self):
        self.player_controller = PlayerController()

    def test_add_player(self):
        # Simulation des entrées utilisateur pour les informations du joueur
        mock_input_data = ['John', 'Doe', '1990-01-01', '123456', '25/12/1980']

        # On substitue input avec une fonction qui retourne chaque élément de mock_input_data
    def mock_input(prompt):
        if mock_input_data:
            birth_date = mock_input_data.pop(0)
            return datetime.strptime(birth_date, '%d/%m/%Y').strftime('%Y-%m-%d')
        else:
            return ''

        # On substitue input avec la fonction mock_input
        original_input = __builtins__.input
        __builtins__.input = mock_input

        # Exécution de la méthode add_player()
        self.player_controller.add_player()

        # Restauration de la fonction input originale
        __builtins__.input = original_input

        # Vérification que la méthode a bien créé un joueur avec les informations fournies
        self.assertIsNotNone(self.player_controller.player)
        self.assertEqual(self.player_controller.player.first_name, 'John')
        self.assertEqual(self.player_controller.player.last_name, 'Doe')
        self.assertEqual(self.player_controller.player.birth_date, '1990-01-01')
        self.assertEqual(self.player_controller.player.national_chess_id, '123456')

        # Vérification que la méthode a bien appelé la méthode save_player() du joueur
        self.assertTrue(self.player_controller.player.save_player_called)

if __name__ == '__main__':
    unittest.main()
