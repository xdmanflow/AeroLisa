# AeroLisa Copilot — RAG Semantic Search

> LLM copilot for aviation maintenance knowledge: RAG semantic search over public maintenance documents with cited answers, then an agent that queries the AeroLisa ontology. Project #3 of AeroLisa.

**Path:** `src/aerolisa/copilot` · **Target:** v1.0 — May 2027 (Project #3)

## Why

Mirrors the Airbus GenAI posting on LLM-based semantic search. Engineers lose time searching manuals and procedures; a grounded assistant that cites its sources saves that time.

## Role in AeroLisa

**Project #3.** Phase 1 is a standalone RAG proof of concept. Phase 2 adds tools so the copilot can answer questions from the platform's own data ("which engines should we inspect this week?").

## Features

- Corpus of public aviation maintenance documents and FAQs
- Chunking, embeddings, vector search (Chroma or FAISS), re-ranking
- Answers with sources; refuses when the corpus has no answer
- Evaluation set of questions with expected answers
- Phase 2: tool calling against the ontology API

## Stack

Python · LangChain or LlamaIndex · Chroma / FAISS · an LLM API · Streamlit · Hugging Face Spaces or Streamlit Cloud

## Data

- Public aviation maintenance documents and FAQs only, each listed with its source and licence in `corpus/sources.md`.

## Roadmap

- [ ] LLM basics + prompting (Apr 24–25, 2027)
- [ ] RAG pipeline (May 1–2)
- [ ] Agent + deployment (May 8–9)
- [ ] Demo video, release v1.0 (May 15–16)

## Definition of done

- [ ] Grounded, correct answers on the evaluation set
- [ ] Usable UI with a public link
- [ ] Architecture diagram + demo video

## Results

_Added at release._
