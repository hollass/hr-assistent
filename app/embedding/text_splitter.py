from typing import List

class TextSplitter:
    def __init__(self, chunk_size: int = 100):
        """
        chunk_size — примерная длина чанка в токенах
        """
        self.chunk_size = chunk_size

    def split(self, text: str) -> List[str]:
        words = text.split()
        chunks = [
            " ".join(words[i:i+self.chunk_size])
            for i in range(0, len(words), self.chunk_size)
        ]
        return chunks
