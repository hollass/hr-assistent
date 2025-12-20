from typing import List

from app.schemas import (
    CandidateProfile,
    RankedCandidate,
    ATSRankingResponse,
)
from app.service.semantic_scorer import SemanticScorer
from app.service.skill_extractor import SkillExtractor


class ATSRanker:
    """
    Ранжирование кандидатов под одну вакансию.
    """

    def __init__(
        self,
        semantic_scorer: SemanticScorer,
        skill_extractor: SkillExtractor,
    ):
        self.semantic = semantic_scorer
        self.skills = skill_extractor

    def rank(
        self,
        jd_text: str,
        candidates: List[CandidateProfile],
        top_k: int | None = None,
    ) -> ATSRankingResponse:

        ranked: List[RankedCandidate] = []

        for candidate in candidates:
            semantic_score = self.semantic.score(
                cv=candidate.cv_text,
                jd=jd_text,
            )

            skill_result = self.skills.match(
                cv=candidate.cv_text,
                jd=jd_text,
            )

            final_score = (
                0.7 * semantic_score.overall_score
                + 0.3 * skill_result.score
            )

            ranked.append(
                RankedCandidate(
                    candidate_id=candidate.candidate_id,
                    score=final_score,
                    semantic=semantic_score,
                    skills=skill_result,
                )
            )

        ranked.sort(key=lambda r: r.score, reverse=True)

        if top_k:
            ranked = ranked[:top_k]

        return ATSRankingResponse(
            jd_text=jd_text,
            results=ranked,
        )
