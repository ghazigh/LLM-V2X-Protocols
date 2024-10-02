# src/semantic_compression.py

import torch
from transformers import AutoModel, AutoTokenizer

class SemanticCompressor:
    def __init__(self, model_name='distilbert-base-uncased'):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)

    def compress(self, text):
        tokens = self.tokenizer(text, return_tensors='pt').to(self.device)
        with torch.no_grad():
            outputs = self.model(**tokens)
        compressed_vector = outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy()
        return compressed_vector

    def decompress(self, compressed_vector):
        # Placeholder for decompression logic
        # Requires a generative model or mapping to reconstruct the message
        return "Decompressed message (not implemented)"