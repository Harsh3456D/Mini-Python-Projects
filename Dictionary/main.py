import requests
import json
import pyttsx3

def meaning(text):
    result = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{text}")
    print(result.content)


meaning("sad")