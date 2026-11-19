# AI Engineer – 30 Days

My hands-on journey from operations leadership (14 years, Meta Payments Operations)
into AI engineering: rebuilding real operations problems as AI systems.

## Day 1 – First LLM programs (local Llama via Ollama)
- `first_llm.py` – first call to a local LLM from Python
- `system_prompt.py` – system prompts, temperature and a simple scope guardrail
- `refund_assistant.py` – **hybrid design**: refund approval thresholds decided by
  deterministic Python rules; the LLM only explains the decision

**Lesson learned:** when the approval rules were inside the prompt, the LLM picked the
wrong approver for a $6,000 refund. Moving the rules into code made decisions correct
and auditable every time. Boundary testing then showed the limits needed `>=` instead of `>`.

## How to run
1. Install [Ollama](https://ollama.com) and run `ollama pull llama3.2:3b`
2. `pip install ollama`
3. `python refund_assistant.py`

## Tech
Python 3.12 · Ollama · Llama 3.2 (3B) · Git