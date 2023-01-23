import json
import requests
import pyttsx3


def call_chatgpt_api(quest):
    auth_token = "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"
    header = {
        "Authorization": "Bearer " + auth_token
    }
    data = {
        "model": "text-davinci-003",
        "prompt": quest,
        "temperature": 1,
        "max_tokens": 500
    }

    # API
    url = "https://api.openai.com/v1/completions"
    resp = requests.post(url, json=data, headers=header)
    return resp.text


def process_response(elements):
    try:
        return json.loads(elements)['choices'][0]['text'].strip() if elements else 'No response.'
    except KeyError:
        return json.loads(elements)['error']['message'].strip()
    except Exception:
        return "Unknown error."


if __name__ == '__main__':
    question = "Qual a raíz quadrada de 144?"
    msg = process_response(call_chatgpt_api(question))
    print(msg)

    engine = pyttsx3.init()
    engine.say(msg)
    engine.runAndWait()
