import unittest
import os
import json
import sys
# Ajout du chemin du répertoire parent pour permettre l'importation des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from Models.Rounds import Round

class TestRound(unittest.TestCase):
    def setUp(self):
        # Création de données de test pour les rounds
        self.matches = [{'player1': 'John', 'player2': 'Doe', 'score': '0-0'},
                        {'player1': 'Alice', 'player2': 'Bob', 'score': '1-0'}]
        self.test_round = Round(round_number=1, round_name='Round 1', matches=self.matches)

    def test_round_initialization(self):
        # Test de l'initialisation de la classe Round
        self.assertEqual(self.test_round.round_number, 1)
        self.assertEqual(self.test_round.round_name, 'Round 1')
        self.assertEqual(self.test_round.matches, self.matches)

    def test_serialize_round(self):
        # Test de la méthode serialize pour vérifier la sérialisation correcte de l'objet Round
        serialized_round = self.test_round.serialize()
        expected_serialized_round = {
            'round_number': 1,
            'round_name': 'Round 1',
            'matches': self.matches
        }
        self.assertEqual(serialized_round, expected_serialized_round)

    def test_save_round(self):
        # Test de la méthode save_round pour vérifier qu'elle ajoute correctement le round au fichier JSON
        # Création d'un round fictif pour simuler l'ajout au fichier JSON
        test_tournament_id = 12345
        test_round = Round(round_number=2, round_name='Round 2', matches=[])
        test_round.save_round(test_tournament_id)

        # Vérification que le round a été ajouté au fichier JSON
        with open('data/tournaments.json', 'r') as file:
            tournaments = json.load(file)
            round_added = False
            for tournament in tournaments:
                if tournament['id'] == test_tournament_id:
                    self.assertIn('round_list', tournament)
                    for round_entry in tournament['round_list']:
                        if round_entry['round_number'] == 2:
                            round_added = True
                            break
                    break
            self.assertTrue(round_added)

    def tearDown(self):
        # Nettoyage des données après les tests
        # Suppression du round ajouté au fichier JSON pendant les tests
        test_tournament_id = 12345
        with open('data/tournaments.json', 'r+') as file:
            tournaments = json.load(file)
            for tournament in tournaments:
                if tournament['id'] == test_tournament_id:
                    tournament['round_list'] = [round_entry for round_entry in tournament['round_list'] if round_entry['round_number'] != 2]
                    break
            file.seek(0)
            file.truncate()
            json.dump(tournaments, file, indent=4)

if __name__ == '__main__':
    unittest.main()
