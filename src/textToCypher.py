from dotenv import load_dotenv
import os
import openai
from training import textToCypherSystemMsg
openai.api_key = os.environ.get('API_KEY')


def genereateCypher(chatHistory):
    messages = [
        {'role': 'system', 'content': textToCypherSystemMsg}
    ] + chatHistory
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    print(completion.choices[0].message)
