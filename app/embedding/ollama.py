import requests
from typing import List
from .base import EmbeddingProvider


class OllamaEmbeddingProvider(EmbeddingProvider):

    def __init__(self, model: str = "nomic-embed-text"):
        self.model = model
        self.url = "http://localhost:11434/api/embeddings"

    def embed(self, text: str) -> List[float]:
        print(text)
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": text
            },
            timeout=30
        )
        response.raise_for_status()
        print(response.json())
        return response.json()["embedding"]

