import unittest
import sys
import os
from io import StringIO
# Ajoute le chemin du répertoire parent pour pouvoir importer les modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Views.Menu import Menu

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()

    def test_main_menu(self):
        # Test si le menu principal est affiché correctement
        with StringIO() as fake_out:
            sys.stdout = fake_out
            self.menu.main_menu()
            output = fake_out.getvalue().strip()

        self.assertIn("CHESS TOURNAMENT MANAGER", output)
        self.assertIn("--- MENU ---", output)
        self.assertIn("1. Ajouter un joueur", output)
        self.assertIn("2. Créer un tournoi", output)
        self.assertIn("3. Ajouter des joueurs à un tournoi", output)
        self.assertIn("4. Lancer un Round", output)
        self.assertIn("5. Rapports", output)
        self.assertIn("0. Quitter", output)

    def test_report_menu(self):
        # Test si le menu des rapports est affiché correctement
        with StringIO() as fake_out:
            sys.stdout = fake_out
            self.menu.report_menu()
            output = fake_out.getvalue().strip()

        self.assertIn("Menu des rapports:", output)
        self.assertIn("1. Liste des joueurs par ordre alphabétique", output)
        self.assertIn("2. Liste des tous les Tournois", output)
        self.assertIn("3. Informations d'un Tournoi", output)
        self.assertIn("4. Liste des joueurs d'un Tournoi", output)
        self.assertIn("5. Détails d'un Tournoi", output)
        self.assertIn("0. Retourner au menu principal", output)

    def tearDown(self):
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
