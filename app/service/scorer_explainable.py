from typing import List, Dict
from app.embedding.ollama import OllamaEmbeddingProvider
from app.embedding.text_splitter import TextSplitter
from app.matching.similarity import cosine_sim

class ExplainableScorer:
    def __init__(self, model: str = "nomic-embed-text", chunk_size: int = 50):
        self.embedding_provider = OllamaEmbeddingProvider(model=model)
        self.splitter = TextSplitter(chunk_size=chunk_size)

    def score_with_attribution(self, cv_text: str, jd_text: str) -> Dict:
        cv_chunks = self.splitter.split(cv_text)
        jd_chunks = self.splitter.split(jd_text)

        jd_embeddings = [self.embedding_provider.embed(chunk) for chunk in jd_chunks]
        jd_vector = [sum(col)/len(col) for col in zip(*jd_embeddings)]

        chunk_scores = []
        for chunk in cv_chunks:
            chunk_vec = self.embedding_provider.embed(chunk)
            score = cosine_sim(chunk_vec, jd_vector)
            chunk_scores.append({"chunk": chunk, "score": score})

        overall_score = sum([c["score"] for c in chunk_scores]) / len(chunk_scores)

        return {
            "overall_score": overall_score,
            "chunk_scores": chunk_scores
        }
