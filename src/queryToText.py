import os
from dotenv import load_dotenv
import openai
from training import queryToTextSystemMsg

load_dotenv()

API_KEY = os.environ.get("API_KEY")
openai.api_key = API_KEY


def generateResponse(chatHistory):
    messages = [
        {'role': 'system', 'content': queryToTextSystemMsg}] + chatHistory
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.0
    )
    response = completion.choices[0].message.content
    return response
