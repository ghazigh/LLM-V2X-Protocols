# src/utils/data_loader.py

import json

def load_sample_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def preprocess_text(text):
    # Implement any text preprocessing steps
    return text.lower()