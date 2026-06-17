# Email Generation Assistant

An AI-powered Email Generation Assistant that generates professional emails from structured user inputs using Large Language Models (LLMs) and prompt engineering techniques.

## Project Overview

This project was developed as part of an AI Engineer assessment. The system generates complete professional emails from three inputs:

* Intent
* Facts
* Tone

The project also evaluates the impact of prompt engineering by comparing:

* **Model A:** Basic Prompt
* **Model B:** Advanced Prompt (Role-Based + Few-Shot Prompting)

---

## Features

* Generate professional emails from structured inputs
* Compare basic and advanced prompting strategies
* Evaluate generated emails using custom metrics
* Automated evaluation and reporting
* JSON and CSV-based outputs

---

## Project Structure

```text
email-generation-assistant/
│
├── data/
│   ├── scenarios.json
│   ├── reference_emails.json
│   ├── model_a_emails.json
│   └── model_b_emails.json
│
├── prompts/
│   ├── basic_prompt.txt
│   └── advanced_prompt.txt
│
├── src/
│   ├── email_generator.py
│   ├── generate_emails.py
│   ├── metrics.py
│   ├── evaluator.py
│   └── compare_models.py
│
├── outputs/
│   ├── model_a_results.csv
│   ├── model_b_results.csv
│   └── results.csv
│
├── requirements.txt
└── README.md
```

---

## Input Format

Each scenario contains:

```json
{
  "id": 1,
  "intent": "Follow up after meeting",
  "facts": [
    "Meeting held June 10",
    "Discussed cloud migration",
    "Need feedback by June 20"
  ],
  "tone": "Professional"
}
```

---

## Prompt Engineering

### Model A – Basic Prompt

```text
Generate a professional email.

Intent:
{intent}

Facts:
{facts}

Tone:
{tone}
```

### Model B – Advanced Prompt

Uses:

* Role-Based Prompting
* Few-Shot Prompting

Example:

```text
You are a Senior Executive Assistant.

Write a professional email that:
- Includes all facts
- Matches the requested tone
- Uses proper email structure
```

---

## Evaluation Metrics

### 1. Fact Recall Score (FRS)

Measures how many required facts appear in the generated email.

Formula:

```text
FRS = Included Facts / Total Facts
```

Range:

```text
0.0 – 1.0
```

---

### 2. Tone Alignment Score (TAS)

Measures how closely the generated email matches the requested tone.

Uses an LLM-as-a-Judge approach.

Range:

```text
0.0 – 1.0
```

---

### 3. Email Structure Quality (ESQ)

Checks for:

* Greeting
* Body
* Closing
* Signature

Formula:

```text
ESQ =
Greeting +
Body +
Closing +
Signature
```

Each component contributes:

```text
0.25
```

Range:

```text
0.0 – 1.0
```

---

## Overall Score

```text
Overall Score =
(FRS + TAS + ESQ) / 3
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd email-generation-assistant
```

### Create Virtual Environment

```bash
python -m venv email
```

### Activate Environment

Windows:

```bash
email\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Generate Emails

```bash
python src/generate_emails.py
```

Outputs:

```text
data/model_a_emails.json
data/model_b_emails.json
```

---

### Evaluate Emails

```bash
python src/evaluator.py
```

Outputs:

```text
outputs/results.csv
```

---

### Compare Models

```bash
python src/compare_models.py
```

Outputs:

```text
outputs/model_a_results.csv
outputs/model_b_results.csv
```

---

## Experimental Results

| Metric                  | Model A | Model B |
| ----------------------- | ------- | ------- |
| Fact Recall Score       | 0.3333  | 0.5333  |
| Tone Alignment Score    | 0.7500  | 0.5500  |
| Email Structure Quality | 0.0000  | 0.0500  |
| Overall Score           | 0.3445  | 0.3778  |

### Key Finding

Model B achieved the highest overall score and demonstrated better fact retention due to advanced prompt engineering techniques.

---

## Technologies Used

* Python
* Hugging Face Transformers
* FLAN-T5
* JSON
* CSV
* Prompt Engineering

---

## Future Improvements

* Use larger instruction-tuned models
* Improve tone evaluation accuracy
* Add semantic fact matching
* Introduce BLEU and ROUGE metrics
* Build a web-based user interface
* Deploy as an API service

---

## Author

Pranto Mondol

AI Engineer Candidate Assessment Project
