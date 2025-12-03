import httpx

url = "https://aipipe.org/openai/v1/chat/completions"
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjIwMDQ1MDhAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.jfLJNzYAKZz60l7CwybGtvKA6WYSNqOxWDAXkrGldeA"
}

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "Analyze the sentiment of the following text. Respond with one of the categories: GOOD, BAD, or NEUTRAL."
        },
        {
            "role": "user",
            "content": "P8 ct7stvoV3Sq C ipv M8 hU1iKM6Q 8  Z 2DgDp6Jnj  x"
        }
    ]
}

response = httpx.post(url, json=payload, headers=headers)
response.raise_for_status()
result = response.json()

print(result)