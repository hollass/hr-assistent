# HR Assistant — Семантическое сравнение CV ↔ JD с Explainability и Skill-level Matching

Минимальный HR-ассистент для семантического сравнения резюме (CV) и описаний вакансий (JD)
с поддержкой различных LLM-эмбеддингов (Ollama, включая Qwen3-VL:4B).

Проект демонстрирует:
- семантическое сравнение текстов
- explainability по чанкам
- skill-level matching
- базовый контроль предвзятости (bias)
- возможность выбора модели эмбеддингов

---

## Проблема

Ручной скрининг резюме занимает много времени и может содержать 
неосознанные предвзятости.  
Рекрутерам приходится тратить часы на чтение CV, которые можно было бы отфильтровать автоматически.

---

## Решение (текущий этап)

- Разбиение CV и JD на чанки  
- Генерация эмбеддингов через Ollama (модель по выбору: `nomic-embed-text`)  
- Семантическая оценка соответствия через cosine similarity  
- Skill-level matching: извлечение и сопоставление навыков CV ↔ JD  
- Explainability: вклад каждого чанка в общий скор  
- Базовая проверка предвзятости (bias detection)

---

## Архитектура

```

CV / JD ──▶ Chunk Split ──▶ Embeddings (Ollama / Qwen3-VL)
│                │
│                └─▶ Cosine Similarity ──▶ Semantic Score
│
├─▶ Skill Extractor ──▶ Skill Score
│
└─▶ LLMAnalyzer (опция: Qwen3-VL) ──▶ Explainability + Bias

````
---

## Стек технологий

- Python 3.10+
- Ollama (локальные LLM эмбеддинги)
- Поддерживаемые модели: `nomic-embed-text`
- NumPy, scikit-learn
- Pydantic (типизированные модели данных)
- Requests (взаимодействие с Ollama API)

---

## Установка

### 1. Установить Ollama
[ollama](https://ollama.com)

### 2. Подгрузить модели
```bash
ollama pull nomic-embed-text
````

### 3. Создать виртуальное окружение

```bash
python -m venv .venv
# Linux / Mac
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

---

## Запуск примера

```bash
python app/main.py
```

Пример запроса модели в CLI:

```
Введите модель Ollama для embeddings (например, 'nomic-embed-text'): nomic-embed-text
```

Пример вывода:

```text
Семантический скор: 0.82
Навыки CV: ['Python', 'FastAPI', 'Django', 'PostgreSQL', 'Docker', 'ML', 'LLM']
Навыки JD: ['Python', 'FastAPI', 'Django', 'PostgreSQL', 'Docker', 'ML']
Совпадающие навыки: ['Python', 'FastAPI', 'Django', 'PostgreSQL', 'Docker', 'ML']
Skill score: 1.0
Проверка предвзятости CV: {'violations': [], 'is_biased': False}
Проверка предвзятости JD: {'violations': [], 'is_biased': False}
```

---

## Текущие ограничения

* Нет полноценной FAIRNESS-логики (только placeholder для слов-признаков)
* Нет REST API / UI
* Поддержка ограничена локальными моделями Ollama

---

## Дорожная карта

* Расширенная FAIRNESS-анализ (гендер, возраст, география)
* REST API через FastAPI + JSON интерфейс
* Визуализация Explainability / Skill-level Matching через Dashboard
* Интеграция других LLM / внешних моделей для embeddings и анализа

---

## Дисклеймер

Проект предназначен **только для образовательных и демонстрационных целей**.
Он **не принимает решения о найме**.

