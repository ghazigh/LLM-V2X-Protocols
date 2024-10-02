# src/models/llm_model.py

import torch.nn as nn

class CustomLLMModel(nn.Module):
    def __init__(self):
        super(CustomLLMModel, self).__init__()
        # Define layers
        self.layer1 = nn.Linear(768, 512)
        self.activation = nn.ReLU()
        self.layer2 = nn.Linear(512, 256)

    def forward(self, x):
        x = self.activation(self.layer1(x))
        x = self.layer2(x)
        return x