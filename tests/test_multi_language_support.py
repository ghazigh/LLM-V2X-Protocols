# tests/test_multi_language_support.py

import unittest
from src.multi_language_support import MultiLanguageSupport

class TestMultiLanguageSupport(unittest.TestCase):
    def setUp(self):
        self.translator = MultiLanguageSupport()

    def test_translate(self):
        text = "This is a test message."
        translated_text = self.translator.translate(text, target_language='fr')
        self.assertIsInstance(translated_text, str)
        self.assertNotEqual(text, translated_text)

if __name__ == '__main__':
    unittest.main()