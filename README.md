# HR Assistant

**HR Assistant** — это инструмент для автоматизации оценки резюме и вакансий с использованием семантических эмбеддингов и анализа навыков. Проект демонстрирует профессиональный подход к этике, fairness и explainability при подборе кандидатов.

---

## 📌 Цели проекта

* Автоматизация ручного скрининга кандидатов
* Семантическое сопоставление CV ↔ JD
* Контроль предвзятости и справедливости
* Explainability: подробные оценки по чанкам текста
* ATS Ranking: ранжирование множества резюме под одну вакансию

---

## 🚀 Фичи

1. **Семантический скоринг**

   * Использует embeddings (Ollama) для измерения сходства между резюме и вакансией
   * Разбивка текста на чанки для explainability

2. **Навыки**

   * Извлечение и сопоставление ключевых навыков из CV и JD
   * Счёт совпадений для оценки релевантности

3. **Bias и fairness**

   * Эвристическая проверка по ключевым признакам (гендер, возраст, национальность)
   * Fairness scoring CV ↔ JD

4. **Explainability**

   * Chunk-based similarity
   * Отдельные оценки по каждому блоку резюме

5. **ATS Ranking**

   * Ранжирование множества резюме под одну вакансию
   * Score = комбинация семантической схожести и навыков
   * Выдаёт топ-K кандидатов с explainability

---

## 🛠 Технологии

* Python 3.10+
* FastAPI (API и документация)
* Pydantic (валидация и схемы)
* Requests (интеграция с Ollama)
* Ollama embeddings (модель `nomic-embed-text`)

---

## 📦 Установка

1. Клонируем репозиторий:

```bash
git clone https://github.com/hollass/hr-assistent.git
cd hr_assistant
```

2. Создаём виртуальное окружение и устанавливаем зависимости:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

3. Устанавливаем и запускаем Ollama:

```bash
ollama pull nomic-embed-text
ollama serve
```

4. Запуск FastAPI:

```bash
uvicorn app.main:app --reload
```

---

## 🔗 API

### 1. Проверка здоровья

```
GET /health
```

**Ответ:**

```json
{"status": "ok"}
```

---

### 2. Сравнение CV ↔ JD

```
POST /match
```

**Тело запроса:**

```json
{
  "cv": "Текст резюме кандидата",
  "jd": "Текст вакансии"
}
```

**Ответ:**

* semantic: SemanticScore
* skills: SkillResult
* fairness: FairnessResult
* llm_insight: LLMInsight (опционально)

---

### 3. ATS Ranking

```
POST /ats/rank
```

**Тело запроса:**

```json
{
  "jd_text": "Текст вакансии",
  "candidates": [
    {"candidate_id": "cv_001", "cv_text": "Резюме 1"},
    {"candidate_id": "cv_002", "cv_text": "Резюме 2"}
  ],
  "top_k": 5
}
```

**Ответ:**

* Список RankedCandidate с score, semantic, skills

---

## ⚡ Использование

1. Создаём экземпляр `AdvancedScorer`:

```python
from app.services.advanced_scorer import AdvancedScorer

scorer = AdvancedScorer()
```

2. Сравнение пары CV ↔ JD:

```python
result = scorer.score(cv="Текст резюме", jd="Текст вакансии")
print(result.semantic.overall_score)
```

3. ATS Ranking для множества резюме:

```python
from app.schemas import CandidateProfile

candidates = [
    CandidateProfile(candidate_id="cv_001", cv_text="Резюме 1"),
    CandidateProfile(candidate_id="cv_002", cv_text="Резюме 2")
]

ranking = scorer.rank_candidates(jd_text="Текст вакансии", candidates=candidates, top_k=3)
print(ranking.results[0].candidate_id)
```

---

## 📊 Архитектура

```
app/
├── main.py           # FastAPI entrypoint
├── api/
│   ├── match.py      # CV ↔ JD
│   └── ats.py        # ATS Ranking
├── services/
│   ├── semantic_scorer.py
│   ├── skill_extractor.py
│   ├── bias_checker.py
│   ├── fairness_analyzer.py
│   ├── llm_analyzer.py
│   ├── advanced_scorer.py
│   └── chunker.py
├── embeddings/
│   ├── base.py
│   └── ollama.py
├── schemas.py
└── core/config.py
```

---

## ✅ Что уже реализовано

* Семантический скоринг с чанкингом
* Skill-aware scoring
* Bias & fairness
* LLM reasoning layer (опционально)
* ATS ranking с top-K
* Explainability по чанкам

