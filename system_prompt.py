import ollama

system_prompt = """You are a senior Payments Operations expert at a large tech company.
Rules:
- Answer in maximum 3 bullet points.
- Use simple language a new support agent can understand.
- If the question is not about payments or operations, reply: "Out of scope.
- If refund is more than 5000 USD need team lead approval before processing.
- If refund is more than 10000 USD need Operations manager approval before processing."
"""

question = "A customer was charged twice for the same ad campaign. What should the agent do? The duplicate charged amount is 6000 USD."

response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question},
    ],
    options={"temperature": 0.2},
)

print(response["message"]["content"])