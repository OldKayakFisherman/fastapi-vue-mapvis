from config import AppSettings
from readers import read_virginia_landmarks
from database import VirginiaLandmarkModel
import os
from typing import List
import unittest

class ReaderTests(unittest.TestCase):

    def test_read_virginia_landmarks(self):

        settings: AppSettings = AppSettings()

        cvs_path = os.path.join(settings.data_dir_root, "Virginia_Landmarks.csv")

        models: List[VirginiaLandmarkModel] = read_virginia_landmarks(cvs_path)

        self.assertIsNotNone(models)
        self.assertGreater(len(models), 0)