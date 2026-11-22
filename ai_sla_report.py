import ollama
from sla_report import load_tickets, add_sla_columns, breach_rate, SLA_HOURS

# 1. Python calculates everything
tickets = add_sla_columns(load_tickets("data/tickets.csv"), SLA_HOURS)

overall = breach_rate(tickets)
by_priority = breach_rate(tickets, "priority")
by_agent = breach_rate(tickets, "agent")
volume = tickets["priority"].value_counts()

facts = f"""Overall breach rate: {overall}%

Breach rate by priority (%):
{by_priority.to_string()}

Breach rate by agent (%):
{by_agent.to_string()}

Ticket volume by priority:
{volume.to_string()}"""

# 2. The LLM only writes, using the given numbers
system_prompt = """You are an operations analyst writing for a payments team lead.
Use ONLY the numbers given. Never calculate or invent new numbers.

Business rules:
- P1 tickets are the most critical (payment failures). Always list P1 risks first,
  even if another priority has a higher breach rate.
- Any agent with a breach rate of 40% or more must be named as a risk.
- Recommended actions must be realistic: staffing, queue allocation, coaching,
  process fixes. Never suggest increasing ticket volume.

Write: 1) a 2-line summary, 2) top 3 risks, 3) 3 recommended actions.
Maximum 150 words."""

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": facts},
    ],
    options={"temperature": 0.2},
)

print("=== FACTS (from Python) ===")
print(facts)
print("\n=== AI REPORT ===")
print(response["message"]["content"])