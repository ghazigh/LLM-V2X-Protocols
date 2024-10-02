# src/multi_language_support.py

from transformers import MarianMTModel, MarianTokenizer

class MultiLanguageSupport:
    def __init__(self, source_lang='en'):
        self.source_lang = source_lang
        self.models = {}

    def translate(self, text, target_language):
        model_name = f'Helsinki-NLP/opus-mt-{self.source_lang}-{target_language}'
        if target_language not in self.models:
            self.tokenizer = MarianTokenizer.from_pretrained(model_name)
            self.model = MarianMTModel.from_pretrained(model_name)
            self.models[target_language] = (self.tokenizer, self.model)
        else:
            self.tokenizer, self.model = self.models[target_language]

        tokens = self.tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')
        translation = self.model.generate(**tokens)
        translated_text = self.tokenizer.batch_decode(translation, skip_special_tokens=True)[0]
        return translated_text