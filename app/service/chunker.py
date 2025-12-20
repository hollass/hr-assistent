from typing import List


class TextChunker:
    def __init__(self, max_chars: int = 500, overlap: int = 50):
        self.max_chars = max_chars
        self.overlap = overlap

    def chunk(self, text: str) -> List[str]:
        text = text.strip()
        if not text:
            return []

        chunks = []
        start = 0
        length = len(text)

        while start < length:
            end = start + self.max_chars
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            start = end - self.overlap

        return chunks
