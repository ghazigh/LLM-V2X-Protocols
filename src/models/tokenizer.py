# src/models/tokenizer.py

class CustomTokenizer:
    def __init__(self, vocab_file):
        with open(vocab_file, 'r') as f:
            self.vocab = f.read().splitlines()
        self.word2idx = {word: idx for idx, word in enumerate(self.vocab)}
        self.idx2word = {idx: word for word, idx in self.word2idx.items()}

    def encode(self, text):
        return [self.word2idx.get(word, self.word2idx['[UNK]']) for word in text.split()]

    def decode(self, indices):
        return ' '.join([self.idx2word.get(idx, '[UNK]') for idx in indices])