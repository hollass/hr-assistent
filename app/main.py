from app.service.scorer_advanced import AdvancedScorer
from app.config import EMBEDDING_MODEL

if __name__ == "__main__":
    cv = """
    Python backend developer, 5 years experience.
    FastAPI, Django, PostgreSQL, Docker.
    Worked with ML and LLM systems.
    """

    jd = """
    Looking for Python backend engineer.
    Required: FastAPI, Docker, PostgreSQL.
    ML experience is a plus.
    """

    scorer = AdvancedScorer(EMBEDDING_MODEL)
    result = scorer.score(cv, jd)

    from pprint import pprint
    pprint(result)
