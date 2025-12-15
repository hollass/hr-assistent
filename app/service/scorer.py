from app.embedding.base import EmbeddingProvider
from app.matching.similarity import cosine_sim
from app.domain.schemas import CV, JobDescription, MatchResult


class CVJDScorer:

    def __init__(self, embedder: EmbeddingProvider):
        self.embedder = embedder

    def score(self, cv: CV, jd: JobDescription) -> MatchResult:
        cv_vec = self.embedder.embed(cv.text)
        jd_vec = self.embedder.embed(jd.text)

        score = cosine_sim(cv_vec, jd_vec)

        return MatchResult(
            score=score,
            model=self.embedder.model
        )