# AI Agent Pipeline Optimization

## Overview

This project demonstrates an optimized multi-agent AI pipeline designed to reduce token usage, improve reliability, and introduce production-ready development practices.

The assignment focuses on:
- AI token/cost optimization
- Agent workflow debugging
- Automated testing and CI/CD setup

---

## Architecture

The pipeline consists of multiple agents:

User Query + Document -> Reader Agent -> Retrieval Agent -> Compression Agent -> Response Validation

### Agents

### Reader Agent
- Reads and prepares input documents.
- Acts as the first stage of the pipeline.

### Retrieval Agent
- Splits documents into smaller chunks.
- Retrieves only relevant information based on the query.
- Reduces unnecessary context processing.

### Compression Agent
- Compresses retrieved information.
- Reduces token consumption while maintaining important context.

---

# Part 1: Token Optimization

## Implemented Optimizations

### 1. Retrieval Before Compression

Instead of processing the complete document, the pipeline first retrieves relevant sections.

Benefits:
- Lower input token usage
- Faster execution
- Reduced AI API cost

### 2. Context Compression

The retrieved information is compressed before generating the final response.

Example Results:

| Stage | Tokens |
|------|--------|
| Original Document | 1664 |
| Retrieved Context | 195 |
| Compressed Output | 130 |

Token Reduction:

- Retrieval saved: **88.28%**
- Compression saved: **33.33%**

---

# Part 2: Debugging and Reliability

Implemented debugging practices:

- Structured logging
- Retry mechanism for failed operations
- Component-level testing
- Response validation
- Fallback handling

The pipeline tracks:
- Execution time
- Token usage
- Agent failures
- Pipeline status

---

# Part 3: CI/CD Pipeline

GitHub Actions workflow automatically performs:

1. Install dependencies
2. Run automated tests
3. Run code quality checks

## Workflow location:

.github/workflows/ci.yml


## Commands executed:

- pytest
- flake8 app

# Testing
## Run tests:

python -m pytest

result:

1 passed

## Run linting:

flake8 app
Project Structure
AI-Agent-Pipeline-Optimization

## Structure

│
├── app
│   ├── agents.py
│   ├── pipeline.py
│   ├── retry.py
│   ├── logger.py
│   └── utils.py
│
├── tests
│   └── test_pipeline.py
│
├── .github
│   └── workflows
│       └── ci.yml
│
├── requirements.txt
├── README.md
└── test.py

## Future Improvements

- Replace keyword retrieval with vector database search (FAISS/ChromaDB)
- Add LLM-based summarization
- Implement monitoring dashboard
- Add staging deployment automation


## Author

Suraj Kembale
