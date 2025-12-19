from typing import List, Optional
import requests

class OllamaEmbeddingProvider:
    """
    Интерфейс для получения эмбеддингов через Ollama.
    """
    def __init__(self, model: str = "nomic-embed-text", host: str = "http://localhost:11434"):
        self.model = model
        self.host = host

    def embed(self, text: str) -> List[float]:
        url = f"{self.host}/api/embeddings"
        payload = {"model": self.model, "prompt": text}
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        if "embedding" in data:
            return data["embedding"]
        if "data" in data and len(data["data"]) > 0 and "embedding" in data["data"][0]:
            return data["data"][0]["embedding"]
        raise ValueError(f"Не удалось получить embedding для модели {self.model}")
