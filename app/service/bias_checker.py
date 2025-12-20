class BiasChecker:
    def __init__(self):
        self.keywords = ["age", "gender", "male", "female", "nationality"]

    def check(self, text: str):
        text = text.lower()
        found = [k for k in self.keywords if k in text]
        return {
            "is_biased": bool(found),
            "violations": found
        }
