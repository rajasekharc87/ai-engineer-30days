import ollama

messages = [
    {"role": "system", "content": "You are a helpful Payments Operations assistant. Keep answers short."}
]

print("Payments assistant ready. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    #### messages.append({"role": "user", "content": user_input})

    response = ollama.chat(model="llama3.2:3b", messages=messages)
    reply = response["message"]["content"]

    ### messages.append({"role": "assistant", "content": reply})
    print("Bot:", reply)