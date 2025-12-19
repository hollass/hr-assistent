import re
from typing import List

class SkillExtractor:
    def __init__(self, skills_list: List[str] = None):
        self.skills_list = skills_list or [
            "Python", "Django", "FastAPI", "PostgreSQL",
            "Docker", "ML", "LLM", "AWS", "Git"
        ]

    def extract(self, text: str) -> List[str]:
        found = []
        text_lower = text.lower()
        for skill in self.skills_list:
            if re.search(rf"\b{skill.lower()}\b", text_lower):
                found.append(skill)
        return found
