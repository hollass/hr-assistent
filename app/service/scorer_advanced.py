from app.service.scorer_explainable import ExplainableScorer
from app.service.skill_extractor import SkillExtractor
from app.service.bias_checker import BiasChecker
from app.llm.llm_analyzer import LLMAnalyzer

class AdvancedScorer:
    def __init__(self, embedding_model: str):
        self.semantic = ExplainableScorer(embedding_model)
        self.skills = SkillExtractor()
        self.bias = BiasChecker()
        self.llm = LLMAnalyzer()

    def score(self, cv_text: str, jd_text: str):
        sem = self.semantic.score_with_attribution(cv_text, jd_text)

        cv_sk = self.skills.extract(cv_text)
        jd_sk = self.skills.extract(jd_text)
        matched = list(set(cv_sk) & set(jd_sk))
        skill_score = len(matched) / max(len(jd_sk), 1)

        result = {
            "semantic_score": sem["overall_score"],
            "chunk_scores": sem["chunk_scores"],
            "cv_skills": cv_sk,
            "jd_skills": jd_sk,
            "matched_skills": matched,
            "skill_score": round(skill_score, 3),
            "bias_baseline": {
                "cv": self.bias.check(cv_text),
                "jd": self.bias.check(jd_text)
            }
        }

        result["llm_analysis"] = self.llm.analyze(cv_text, jd_text, result)
        return result
