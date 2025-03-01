from converters import convert_string_to_bool
import unittest

class ConverterTests(unittest.TestCase):

    def test_convert_string_to_bool(self):
        self.assertFalse(convert_string_to_bool("False"))
        self.assertFalse(convert_string_to_bool("false"))
        self.assertTrue(convert_string_to_bool("True"))
        self.assertTrue(convert_string_to_bool("true"))
        self.assertFalse(convert_string_to_bool("F"))
        self.assertFalse(convert_string_to_bool("f"))
        self.assertTrue(convert_string_to_bool("T"))
        self.assertTrue(convert_string_to_bool("t"))
        self.assertTrue(convert_string_to_bool("1"))
        self.assertFalse(convert_string_to_bool("0"))