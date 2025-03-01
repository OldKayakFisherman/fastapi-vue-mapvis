from config import AppSettings
import unittest

class ConfigTests(unittest.TestCase):

    def test_get_settings(self):
        settings: AppSettings = AppSettings()

        self.assertIsNotNone(settings)
        self.assertIsNotNone(settings.data_dir_root)
        self.assertIsNotNone(settings.db_filename)
        self.assertIsNotNone(settings.db_filepath)
        self.assertIsNotNone(settings.db_connection_string)