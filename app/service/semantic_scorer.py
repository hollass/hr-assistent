import math
from typing import List

from app.schemas import SemanticScore, ChunkScore
from app.embeddings.base import EmbeddingProvider
from app.service.chunker import TextChunker


def cosine_similarity(a: List[float], b: List[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    return dot / (norm_a * norm_b + 1e-9)


class SemanticScorer:

    def __init__(
        self,
        provider: EmbeddingProvider,
        chunker: TextChunker | None = None,
    ):
        self.provider = provider
        self.chunker = chunker or TextChunker()

    def score(self, cv: str, jd: str) -> SemanticScore:
        cv_chunks = self.chunker.chunk(cv)
        jd_chunks = self.chunker.chunk(jd)

        if not cv_chunks or not jd_chunks:
            return SemanticScore(overall_score=0.0, chunk_scores=[])

        cv_embeddings = [self.provider.embed(c) for c in cv_chunks]
        jd_embeddings = [self.provider.embed(j) for j in jd_chunks]

        chunk_scores: list[ChunkScore] = []
        similarities: list[float] = []

        for i, cv_emb in enumerate(cv_embeddings):
            best_sim = 0.0
            for jd_emb in jd_embeddings:
                sim = cosine_similarity(cv_emb, jd_emb)
                best_sim = max(best_sim, sim)

            similarities.append(best_sim)
            chunk_scores.append(
                ChunkScore(
                    chunk_index=i,
                    similarity=best_sim,
                )
            )

        overall = sum(similarities) / len(similarities)

        return SemanticScore(
            overall_score=overall,
            chunk_scores=chunk_scores,
        )
