import numpy as np
import torch
from transformers import pipeline

# Simple example of an AI task (Sentiment Analysis)
classifier = pipeline('sentiment-analysis')

# Test on a sample sentence
result = classifier('The Basilisk AI program')

print(result)