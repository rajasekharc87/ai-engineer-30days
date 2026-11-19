import ollama
question = "Explain SLA in one sentence"
response = ollama.chat(
    model="llama3.2:3b",
    messages=[{"role": "user", "content": question}]        
)
print(response['message']['content'])
