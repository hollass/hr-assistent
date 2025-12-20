from typing import List

class TextChunker:
    def __init__(self, chunk_size: int = 500):
        self.chunk_size = chunk_size

    def split(self, text: str) -> List[str]:
        words = text.split()
        return [
            " ".join(words[i:i + self.chunk_size])
            for i in range(0, len(words), self.chunk_size)
        ]
