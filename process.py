import load_env as e

import openai

API_KEY =  e.get_key()

openai.api_key = API_KEY

prompt = """
I will give you prompts with Indonesian language. Here's the prompt:

Tentukan apakah tweet-tweet yang diberikan adalah positif, netral, atau negatif (Sentiment Analysis). Berikut list tweets-nya:

1. "Aku ga kuat dengan pekerjaan rumah"
2. "Ini payah. Aku bosen 😠"
3. "Aku tidak sabar menunggu Halloween!!!"
4. "Kucingku lucu bangett ❤️❤️"
5. "selain di gedor mereka juga bilang gini "kok lama? main lato lato ya? ajarin lato lato dong" ANJING AJJING"

Tweet sentiment ratings:
"""

# result: (taken from "first-result.txt")
# "1. Negatif\n2. Negatif\n3. Positif\n4. Positif\n5. Negatif"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
)

print(response)