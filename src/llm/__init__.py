from transformers import pipeline
from .classifier import classify

llm = pipeline("zero-shot-classification",
               model="facebook/bart-large-mnli")

__all__ = ['classify']
