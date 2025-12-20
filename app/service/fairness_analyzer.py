from app.schemas import FairnessBlock, FairnessScore


class FairnessAnalyzer:
    def analyze(self, cv: str, jd: str) -> FairnessBlock:
        return FairnessBlock(
            cv=FairnessScore(
                gender=0.1,
                age=0.0,
                nationality=0.0,
            ),
            jd=FairnessScore(
                gender=0.3,
                age=0.2,
                nationality=0.1,
            ),
        )
