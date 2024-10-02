# tests/test_context_aware_messaging.py

import unittest
from src.context_aware_messaging import ContextAwareMessenger

class TestContextAwareMessaging(unittest.TestCase):
    def setUp(self):
        self.messenger = ContextAwareMessenger()

    def test_create_and_parse_message(self):
        compressed_message = [0.1, 0.2, 0.3]
        context = {"location": "Testville", "priority": "Low"}
        context_message = self.messenger.create_message(compressed_message, context)
        parsed_message, parsed_context = self.messenger.parse_message(context_message)
        self.assertEqual(compressed_message, parsed_message)
        self.assertEqual(context, parsed_context)

if __name__ == '__main__':
    unittest.main()