import os
import gc
import pickle
import urllib.request
import numpy as np
import pandas as pd
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from transformers import RobertaTokenizer, RobertaForSequenceClassification

class ReadabilityPredictor:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.folder_path = None
        self.weight_path = None
        self.model = None
        self.tokenizer = None
        self.load_model()

    def load_model(self):
        """Load the model and tokenizer based on the selected model name."""
        if self.model_name == 'DistilBERT':
            self.folder_path = 'output/v59/'
            self.weight_path = 'https://github.com/kozodoi/Kaggle_Readability/releases/download/0e96d53/weights_v59.pth'
            self.tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")
            self.model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")
        elif self.model_name == 'DistilRoBERTa':
            self.folder_path = 'output/v47/'
            self.weight_path = 'https://github.com/kozodoi/Kaggle_Readability/releases/download/0e96d53/weights_v47.pth'
            self.tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
            self.model = RobertaForSequenceClassification.from_pretrained("roberta-base")

        # Download model weights if not already present
        if not os.path.isfile(os.path.join(self.folder_path, 'pytorch_model.bin')):
            self.download_weights()

        self.model.eval()

    def download_weights(self):
        """Download model weights from the specified URL."""
        os.makedirs(self.folder_path, exist_ok=True)
        urllib.request.urlretrieve(self.weight_path, os.path.join(self.folder_path, 'pytorch_model.bin'))

    def compute_readability(self, input_text: str) -> float:
        """Compute the readability score for the input text."""
        if input_text.strip() == "":
            return 0.0  # Avoid processing empty input

        # Tokenize input text
        tokens = self.tokenizer(
            input_text,
            truncation=True,
            padding=True,
            max_length=512,
            return_tensors='pt'
        )

        with torch.no_grad():
            # Compute prediction
            outputs = self.model(**tokens)
            prediction = outputs.logits[0][0].item()
            # Scale to [0, 100]
            readability_score = 100 * (prediction + 4) / 6  # Adjust scaling

        return readability_score
