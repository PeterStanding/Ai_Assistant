#Installed Gemma3 Package

import ollama

client = ollama.Client()

model = "gemma3"
prompt = "What is Python?"

response = client.generate(model = model, prompt = prompt)

print("Response from Ollama:")
print(response.response)