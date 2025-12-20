from app.schemas import MatchResponse, FairnessResult, CandidateProfile, ATSRankingResponse
from app.service.semantic_scorer import SemanticScorer
from app.service.skill_extractor import SkillExtractor
from app.service.bias_checker import BiasChecker
from app.service.fairness_analyzer import FairnessAnalyzer
from app.service.llm_analyzer import LLMAnalyzer
from app.embeddings.ollama import OllamaEmbeddingProvider
from app.service.ats_ranker import ATSRanker


class AdvancedScorer:

    def __init__(self):
        embedding_provider = OllamaEmbeddingProvider(
            model="nomic-embed-text"
        )

        self.semantic = SemanticScorer(embedding_provider)
        self.skills = SkillExtractor()
        self.bias = BiasChecker()
        self.fairness = FairnessAnalyzer()
        self.llm = LLMAnalyzer()
        self.ats_ranker = ATSRanker(
            semantic_scorer=self.semantic,
            skill_extractor=self.skills,
        )

    def score(self, cv: str, jd: str) -> MatchResponse:
        semantic_score = self.semantic.score(cv, jd)
        skill_result = self.skills.match(cv, jd)

        bias_jd = self.bias.check(jd)
        fairness_block = self.fairness.analyze(cv, jd)

        return MatchResponse(
            semantic=semantic_score,
            skills=skill_result,
            fairness=FairnessResult(
                baseline=bias_jd,
                scoring=fairness_block,
            ),
            llm_insight=self.llm.analyze(),
        )

    def rank_candidates(
            self,
            jd_text: str,
            candidates: list[CandidateProfile],
            top_k: int | None = None,
    ) -> ATSRankingResponse:
        return self.ats_ranker.rank(
            jd_text=jd_text,
            candidates=candidates,
            top_k=top_k,
        )
