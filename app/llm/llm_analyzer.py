import requests
from app.config import OLLAMA_HOST, LLM_MODEL

class LLMAnalyzer:
    def analyze(self, cv_text, jd_text, scores):
        prompt = f"""
Ты HR-ассистент и эксперт по этичному найму.

Semantic score: {scores['semantic_score']}
Skill score: {scores['skill_score']}
Matched skills: {scores['matched_skills']}

1. Объясни соответствие кандидата вакансии
2. Найди пробелы в навыках
3. Найди потенциальный bias
4. Дай рекомендацию

Ответ строго в JSON:
{{
  "summary": "...",
  "skill_gaps": [],
  "bias_risks": [],
  "recommendation": "..."
}}
"""

        r = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={
                "model": LLM_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        r.raise_for_status()
        return r.json()
