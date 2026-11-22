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

## Day 2 – SLA analytics with Pandas + AI-written report
- `explore_tickets.py` – data exploration and data-quality checks (missing agents flagged as "Unassigned")
- `sla_report.py` – reusable functions: load tickets, add SLA columns, breach rate overall or by group
- `ai_sla_report.py` – Python computes all metrics; the LLM writes a team-lead summary

**Lessons learned:** averaging per-agent percentages gives the wrong overall rate (25.7% vs the true 28.4%) –
always compute from totals. The LLM kept numbers correct when grounded, but its first report suggested
"increase ticket volume" and missed a 50%-breach agent; adding domain rules to the prompt fixed most issues,
and remaining rules are better enforced in code.

## How to run
1. Install [Ollama](https://ollama.com) and run `ollama pull llama3.2:3b`
2. `pip install ollama`
3. `python refund_assistant.py`

## Tech
Python 3.12 · Ollama · Llama 3.2 (3B) · Git
