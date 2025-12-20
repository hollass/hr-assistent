from app.schemas import SkillResult, SkillMatch


class SkillExtractor:
    """
    Извлечение и сопоставление навыков.
    """
    def extract(self, text: str) -> list[str]:
        keywords = ["python", "fastapi", "sql", "docker"]
        text_lower = text.lower()
        return [k for k in keywords if k in text_lower]

    def match(self, cv: str, jd: str) -> SkillResult:
        cv_skills = self.extract(cv)
        jd_skills = self.extract(jd)

        matched = [
            SkillMatch(skill=s)
            for s in cv_skills
            if s in jd_skills
        ]

        score = len(matched) / max(len(jd_skills), 1)

        return SkillResult(
            cv_skills=cv_skills,
            jd_skills=jd_skills,
            matched=matched,
            score=score,
        )
