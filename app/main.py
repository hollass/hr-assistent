from app.service.scorer_advanced import AdvancedScorer
from app.embedding.embedding_ollama import OllamaEmbeddingProvider

if __name__ == "__main__":
    user_model = input(
        "Введите модель Ollama для embeddings (например, 'nomic-embed-text' или 'qwen3-vl:4b'): ").strip()

    scorer = AdvancedScorer(embedding_model=user_model)

    cv_text = """
    Опыт работы Python backend разработчиком 5 лет.
    Знаком с FastAPI, Django, PostgreSQL, Docker.
    Работал с ML-проектами и LLM.
    """
    jd_text = """
    Ищем Python backend разработчика.
    Опыт с FastAPI, Django, Docker, PostgreSQL.
    Желателен опыт работы с ML.
    """

    result = scorer.score(cv_text, jd_text)

    print("Семантический скор:", result["semantic_score"])
    print("Навыки CV:", result["cv_skills"])
    print("Навыки JD:", result["jd_skills"])
    print("Совпадающие навыки:", result["matched_skills"])
    print("Skill score:", result["skill_score"])
    print("Проверка предвзятости CV:", result["bias_cv"])
    print("Проверка предвзятости JD:", result["bias_jd"])
