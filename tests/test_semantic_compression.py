# tests/test_semantic_compression.py

import unittest
from src.semantic_compression import SemanticCompressor

class TestSemanticCompression(unittest.TestCase):
    def setUp(self):
        self.compressor = SemanticCompressor()

    def test_compress(self):
        message = "Test message for semantic compression."
        compressed = self.compressor.compress(message)
        self.assertIsNotNone(compressed)
        self.assertEqual(len(compressed.shape), 1)

    def test_decompress(self):
        compressed = [0.5] * 768  # Mock compressed vector
        decompressed = self.compressor.decompress(compressed)
        self.assertIsInstance(decompressed, str)

if __name__ == '__main__':
    unittest.main()