import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrenchEq(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestEnglishToFrenchNeq(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french("Hello"), "Hello")

class TestFrenchToEnglisheq(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

class TestFrenchToEnglishNeq(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

unittest.main(verbosity=2)
