from fastapi import APIRouter
from app.schemas import (
    CandidateProfile,
    ATSRankingResponse,
)
from app.service.scorer_advanced import AdvancedScorer

router = APIRouter(prefix="/ats")
scorer = AdvancedScorer()


@router.post("/rank", response_model=ATSRankingResponse)
def rank_candidates(
        jd_text: str,
        candidates: list[CandidateProfile],
        top_k: int | None = None,
) -> ATSRankingResponse:
    return scorer.rank_candidates(
        jd_text=jd_text,
        candidates=candidates,
        top_k=top_k,
    )
