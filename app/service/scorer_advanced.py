from typing import Dict
from .scorer_explainable import ExplainableScorer
from .skill_extractor import SkillExtractor
from .bias_checker import BiasChecker

class AdvancedScorer:
    def __init__(self, embedding_model: str = "nomic-embed-text"):
        self.semantic_scorer = ExplainableScorer(model=embedding_model)
        self.skill_extractor = SkillExtractor()
        self.bias_checker = BiasChecker()

    def score(self, cv_text: str, jd_text: str) -> Dict:
        sem_result = self.semantic_scorer.score_with_attribution(cv_text, jd_text)

        cv_skills = self.skill_extractor.extract(cv_text)
        jd_skills = self.skill_extractor.extract(jd_text)

        matched_skills = list(set(cv_skills) & set(jd_skills))
        skill_score = len(matched_skills) / max(len(jd_skills), 1)

        bias_cv = self.bias_checker.check(cv_text)
        bias_jd = self.bias_checker.check(jd_text)

        return {
            "semantic_score": sem_result["overall_score"],
            "chunk_scores": sem_result["chunk_scores"],
            "cv_skills": cv_skills,
            "jd_skills": jd_skills,
            "matched_skills": matched_skills,
            "skill_score": skill_score,
            "bias_cv": bias_cv,
            "bias_jd": bias_jd
        }
