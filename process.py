import load_env as e
import openai
import keyword_generator as key_gen

API_KEY =  e.get_key()

openai.api_key = API_KEY

DESIGN_PROMPT = """
Act as an expert in the topic and provide insightful and detailed responses to questions related to the topic. You will choose the topic based on the keywords. I will provide the keywords in a list format, and you will give informative and detail responses, including relevant information, context and any other details that might be necessary. Your responses should demonstrate a deep understanding of the topic and be presented in a teaching and scholarly manner. Please avoid providing general information or summaries. 

"""

DESIGN_PROMPT_2 = f"""
Provide me short and related insight between keywords: 
"""

keywords = key_gen.get_keywords()

prompt = f"""
The keywords are:
{keywords}
"""

prompt2 = str(keywords)

# final_prompt = DESIGN_PROMPT + prompt
final_prompt = DESIGN_PROMPT_2 + prompt2

print('final prompt: ', final_prompt)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=final_prompt,
  temperature=0.3,
  max_tokens=512,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
)

print(response)