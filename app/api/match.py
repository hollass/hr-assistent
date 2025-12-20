from fastapi import APIRouter
from app.schemas import MatchResponse
from app.service.scorer_advanced import AdvancedScorer

router = APIRouter()
scorer = AdvancedScorer()


@router.post("/match", response_model=MatchResponse)
def match(cv: str, jd: str) -> MatchResponse:
    """
    Сравнение резюме и вакансии.
    """
    return scorer.score(cv, jd)
