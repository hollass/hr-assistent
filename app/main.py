from embedding.ollama import OllamaEmbeddingProvider
from service.scorer import CVJDScorer
from domain.schemas import CV, JobDescription


if __name__ == "__main__":
    cv = CV(text="Python developer with 3 years of experience in backend systems")
    jd = JobDescription(text="Looking for a backend engineer with Python experience")

    embedder = OllamaEmbeddingProvider()
    scorer = CVJDScorer(embedder)

    result = scorer.score(cv, jd)
    print(result)