# tests/test_end_to_end.py

import unittest
from src.semantic_compression import SemanticCompressor
from src.context_aware_messaging import ContextAwareMessenger
from src.multi_language_support import MultiLanguageSupport

class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        self.compressor = SemanticCompressor()
        self.messenger = ContextAwareMessenger()
        self.translator = MultiLanguageSupport()

    def test_full_pipeline(self):
        message = "Emergency vehicle approaching."
        context = {"location": "5th Avenue", "direction": "Northbound"}
        compressed = self.compressor.compress(message)
        context_message = self.messenger.create_message(compressed, context)
        translated_message = self.translator.translate(str(context_message), target_language='es')
        self.assertIsInstance(translated_message, str)

if __name__ == '__main__':
    unittest.main()