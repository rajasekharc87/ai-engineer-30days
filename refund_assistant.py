import ollama
refund_amount = 15000
#Business rule decided by the code not by LLM
if refund_amount >= 10000:
    approval_required = "Operations manager approval"
elif refund_amount >= 5000:
    approval_required = "Team lead approval"
else:
    approval_required = "No approval required"
system_prompt = """You are a senior Payments Operations expert.
Answer in maximum 3 bullet points, in simple language for a new support agent.
Use the approval decision exactly as given. Never change it."""

question = f"""A customer was charged twice for the same ad campaign.
Refund amount: ${refund_amount}
Approval required: {approval_required}
What should the agent do?"""

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ],
    options={"temperature": 0.1},
)

print("Approver decided by rules:", approval_required)
print(response["message"]["content"])