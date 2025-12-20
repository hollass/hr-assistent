# HR Assistant — Semantic CV ↔ JD Matching with Explainability & Fairness

HR-ассистент для автоматизированного анализа соответствия резюме (CV) и описаний вакансий (JD).
Проект использует **эмбеддинги для численного скоринга** и **LLM (через Ollama) для
reasoning, explainability и этического анализа**.

Проект ориентирован на демонстрацию:
- гибридных LLM-пайплайнов (embeddings + reasoning),
- explainability решений,
- контроля bias и fairness,
- production-ориентированной архитектуры.

---

## Проблема

Ручной скрининг резюме:
- плохо масштабируется,
- подвержен субъективным ошибкам,
- сложен для аудита и объяснения решений.

---

## Решение

Многоуровневый HR-ассистент:

1. **Детерминированный анализ**
   - семантическое сравнение CV ↔ JD через embeddings,
   - chunk-based explainability,
   - skill-level matching.

2. **LLM-анализ**
   - человеко-читаемое объяснение результата,
   - выявление skill gaps,
   - анализ потенциальной дискриминации,
   - рекомендации рекрутеру.

---

## Архитектура

```

CV / JD
│
├─▶ Chunking
│     └─▶ Embeddings (embedding-модель)
│            └─▶ Cosine Similarity
│                   └─▶ Semantic Score + Chunk attribution
│
├─▶ Skill Extraction
│     └─▶ Skill Match Score
│
└─▶ LLM Analyzer
├─▶ Explainability
├─▶ Bias / Fairness analysis
└─▶ Hiring recommendation

````

---

## Технологический стек

- Python 3.10+
- Ollama
- Embedding-модель: `nomic-embed-text` (или аналогичная)
- LLM (reasoning): `qwen3-vl:4b` (или аналогичная)
- NumPy
- Requests

---

## Установка

### 1. Установить Ollama
https://ollama.com

### 2. Загрузить модели
```bash
ollama pull nomic-embed-text (или аналогичная)
ollama pull qwen3-vl:4b (или аналогичная)
````

### 3. Виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows
```

### 4. Зависимости

```bash
pip install -r requirements.txt
```

---

## Запуск

```bash
python app/main.py
```

Пример результата:

* semantic score (численный),
* вклад каждого чанка,
* совпадающие навыки,
* LLM-объяснение и рекомендации.

---

## Ключевые особенности проекта

* Чёткое разделение:

  * embeddings → математика,
  * LLM → reasoning и этика.
* Explainability на уровне модели и текста.
* Bias / fairness как часть пайплайна.
* Реалистичный HR-use-case, применимый к ATS.

---

## Ограничения

* Fairness-анализ пока эвристический и LLM-based.
* Нет REST API и UI (планируется).
* Проект не принимает автоматических решений о найме.

---

## Roadmap

* REST API (FastAPI)
* Batch-оценка резюме
* Fairness v2 (LLM + embedding сигнал)
* Визуализация explainability
* Подготовка к production deployment

---

## Disclaimer

Проект предназначен **исключительно для демонстрационных и образовательных целей**.
Он **не должен использоваться для автоматического принятия решений о найме**.

