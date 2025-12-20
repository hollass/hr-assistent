from app.schemas import LLMInsight


class LLMAnalyzer:

    def analyze(self) -> LLMInsight:
        return LLMInsight(
            summary="Кандидат в целом соответствует вакансии.",
            skill_gaps=["docker"],
            fairness_risks=["gender bias in JD"],
            recommendation="Рекомендуется к следующему этапу.",
        )
