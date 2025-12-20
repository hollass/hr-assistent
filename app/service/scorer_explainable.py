from typing import Dict, List
from app.embedding.embedding_ollama import OllamaEmbeddingProvider
from app.service.chunker import TextChunker
from app.utils.similarity import cosine_similarity

class ExplainableScorer:
    def __init__(self, model: str):
        self.embedder = OllamaEmbeddingProvider(model)
        self.chunker = TextChunker()

    def score_with_attribution(self, cv_text: str, jd_text: str) -> Dict:
        cv_chunks = self.chunker.split(cv_text)
        jd_embedding = self.embedder.embed(jd_text)

        chunk_scores = []
        for chunk in cv_chunks:
            emb = self.embedder.embed(chunk)
            score = cosine_similarity(emb, jd_embedding)
            chunk_scores.append({
                "chunk": chunk,
                "score": round(score, 4)
            })

        overall = sum(c["score"] for c in chunk_scores) / len(chunk_scores)

        return {
            "overall_score": round(overall, 4),
            "chunk_scores": chunk_scores
        }
