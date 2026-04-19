import requests
import json

def meaning(text):
    result = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{text}")
    data = result.json()
    print(json.dumps(data, indent=4))


meaning("sad")
