import requests
from typing import List

from app.embeddings.base import EmbeddingProvider


class OllamaEmbeddingProvider(EmbeddingProvider):
    """
    Embedding через Ollama.
    Пользователь сам указывает модель (например: nomic-embed-text).
    """

    def __init__(
        self,
        base_url: str = "http://localhost:11434",
        model: str = "nomic-embed-text",
        timeout: int = 30,
    ):
        self.base_url = base_url
        self.model = model
        self.timeout = timeout

    def embed(self, text: str) -> List[float]:
        url = f"{self.base_url}/api/embeddings"

        payload = {
            "model": self.model,
            "prompt": text,
        }

        response = requests.post(url, json=payload, timeout=self.timeout)
        response.raise_for_status()

        data = response.json()

        if "embedding" not in data:
            raise RuntimeError(f"Invalid Ollama response: {data}")

        return data["embedding"]
