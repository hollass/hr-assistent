from typing import Dict

class BiasChecker:
    def __init__(self):
        self.forbidden_keywords = ['возраст', 'лет', 'годов']

    def check(self, text: str) -> Dict:
        violations = [kw for kw in self.forbidden_keywords if kw in text.lower()]
        return {"violations": violations, "is_biased": len(violations) > 0}
