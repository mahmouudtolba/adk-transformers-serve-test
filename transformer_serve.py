
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="<random_string>")

completion = client.chat.completions.create(
    model="./models/Qwen_Qwen3-0.6B",
    messages=[
        {
            "role": "user",
            "content": "What is the Transformers library known for?"
        }
    ],
    stream=True
)

for chunk in completion:
    token = chunk.choices[0].delta.content
    if token:
        print(token, end='')