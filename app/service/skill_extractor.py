import re
from typing import List

class SkillExtractor:
    def __init__(self):
        self.skills = [
            "python", "fastapi", "django", "postgresql",
            "docker", "ml", "llm", "aws", "git"
        ]

    def extract(self, text: str) -> List[str]:
        text = text.lower()
        return [s.capitalize() for s in self.skills if re.search(rf"\b{s}\b", text)]
