from app.schemas import BiasBaseline, BiasResult


class BiasChecker:

    def check(self, text: str) -> BiasBaseline:
        gender_terms = ["he", "she", "man", "woman"]
        age_terms = ["young", "old", "age"]
        nationality_terms = ["nationality", "citizen"]

        text_lower = text.lower()

        return BiasBaseline(
            gender=BiasResult(
                keywords_found=[k for k in gender_terms if k in text_lower],
                risk=any(k in text_lower for k in gender_terms),
            ),
            age=BiasResult(
                keywords_found=[k for k in age_terms if k in text_lower],
                risk=any(k in text_lower for k in age_terms),
            ),
            nationality=BiasResult(
                keywords_found=[k for k in nationality_terms if k in text_lower],
                risk=any(k in text_lower for k in nationality_terms),
            ),
        )
