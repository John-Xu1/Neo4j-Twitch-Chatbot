from dotenv import load_dotenv
import os
import openai
from training import textToCypherSystemMsg

load_dotenv()
openai.api_key = os.environ.get('API_KEY')


def genereateCypher(chatHistory):
    messages = [
        {'role': 'system', 'content': textToCypherSystemMsg}
    ] + chatHistory
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    cypher = str(completion.choices[0].message.content)
    print(cypher)
    return cypher
