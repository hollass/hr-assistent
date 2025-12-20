from app.embeddings.ollama import OllamaEmbeddingProvider
from app.service.chunker import TextChunker
from app.schemas import SemanticScore, ChunkScore
from app.service.semantic_scorer import cosine_similarity


class ExplainableScorer:
    def __init__(self, model: str):
        self.embedder = OllamaEmbeddingProvider(model)
        self.chunker = TextChunker()

    def score_with_attribution(self, cv_text: str, jd_text: str) -> SemanticScore:
        cv_chunks = self.chunker.split(cv_text)
        jd_embedding = self.embedder.embed(jd_text)

        chunk_scores: list[ChunkScore] = [...]
        for chunk in cv_chunks:
            emb = self.embedder.embed(chunk)
            score = cosine_similarity(emb, jd_embedding)
            chunk_scores.append({
                "chunk": chunk,
                "score": round(score, 4)
            })

        overall = sum(c["score"] for c in chunk_scores) / len(chunk_scores)

        return SemanticScore(
            overall_score=overall,
            chunk_scores=chunk_scores
        )
