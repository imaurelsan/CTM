import unittest
import os
import sys
# Ajout du chemin du répertoire parent pour permettre l'importation des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.Tournament import Tournament


class TestTournament(unittest.TestCase):
    def setUp(self):
        self.test_tournament = Tournament(
            name="Test Tournament",
            location="Test Location",
            start_date="2024-01-01",
            end_date="2024-01-07"
        )

    def tearDown(self):
        if os.path.exists('data/tournaments.json'):
            os.remove('data/tournaments.json')

    def test_save_tournament(self):
        self.test_tournament.save_tournament()

        # Vérifier si le fichier a été créé
        self.assertTrue(os.path.exists('data/tournaments.json'))

        # Vérifier si le contenu du fichier est correct
        with open('data/tournaments.json', 'r') as file:
            tournaments = file.read()
            self.assertIn("Test Tournament", tournaments)

    def test_get_tournaments(self):
        # Vérifier si la méthode retourne une liste de tournois
        tournaments = self.test_tournament.get_tournaments()
        self.assertIsInstance(tournaments, list)

        # Vérifier si la méthode retourne un message d'erreur si le fichier n'existe pas
        os.remove('data/tournaments.json')
        error_message = self.test_tournament.get_tournaments()
        self.assertEqual(error_message, 'Le fichier tournaments.json est introuvable')

    def test_update_tournament(self):
        # Ajouter un tournoi pour être mis à jour
        self.test_tournament.save_tournament()

        # Mettre à jour le tournoi ajouté
        updated_tournament = {
            'id': self.test_tournament.id,
            'name': 'Updated Test Tournament',
            'location': 'Updated Test Location',
            'start_date': '2024-01-01',
            'end_date': '2024-01-07'
        }
        self.test_tournament.update_tournament(updated_tournament)

        # Vérifier si le tournoi a été mis à jour correctement
        tournaments = self.test_tournament.get_tournaments()
        for tournament in tournaments:
            if tournament['id'] == self.test_tournament.id:
                self.assertEqual(tournament['name'], 'Updated Test Tournament')
                self.assertEqual(tournament['location'], 'Updated Test Location')
                break
        else:
            self.fail("Le tournoi n'a pas été mis à jour correctement")


if __name__ == '__main__':
    unittest.main()
