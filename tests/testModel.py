import unittest
import sys
import json
import os
# Ajout du chemin du répertoire parent pour permettre l'importation des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.Model import Model


class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()
        self.data_file_path_existing = 'data_existing.json'
        self.data_file_path_empty = 'data_empty.json'
        self.data_file_path_not_exist = 'data_not_exist.json'

    def tearDown(self):
        # Nettoyer les fichiers de données créés pendant les tests
        for file_path in [self.data_file_path_existing, self.data_file_path_empty]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_get_new_id_existing_data(self):
        # Cas de test : Fichier de données existant avec des éléments
        # Créer un fichier de données avec des éléments
        with open(self.data_file_path_existing, 'w') as file:
            json.dump([{'id': 1}, {'id': 2}], file)

        new_id = self.model.get_new_id(self.data_file_path_existing)
        # Vérifier que le nouvel ID est unique et correct
        self.assertEqual(new_id, 3)

    def test_get_new_id_empty_data(self):
        # Cas de test : Fichier de données existant mais vide
        # Créer un fichier de données vide
        with open(self.data_file_path_empty, 'w') as file:
            json.dump([], file)

        new_id = self.model.get_new_id(self.data_file_path_empty)
        # Vérifier que le nouvel ID est 1
        self.assertEqual(new_id, 1)

    def test_get_new_id_non_existing_file(self):
        # Cas de test : Fichier de données n'existe pas
        new_id = self.model.get_new_id(self.data_file_path_not_exist)
        # Vérifier que le nouvel ID est 1
        self.assertEqual(new_id, 1)


if __name__ == '__main__':
    unittest.main()
