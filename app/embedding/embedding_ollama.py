import requests
from typing import List
from app.config import OLLAMA_HOST

class OllamaEmbeddingProvider:
    def __init__(self, model: str):
        self.model = model

    def embed(self, text: str) -> List[float]:
        response = requests.post(
            f"{OLLAMA_HOST}/api/embeddings",
            json={
                "model": self.model,
                "prompt": text
            }
        )
        response.raise_for_status()
        return response.json()["embedding"]
