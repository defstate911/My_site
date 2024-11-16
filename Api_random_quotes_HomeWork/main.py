from flask import Flask, render_template
import requests
from translate import Translator

app = Flask(__name__)

def get_random_quote():
    api_url = "https://api.quotable.io/random"
    try:
        response = requests.get(api_url, verify=False)
        response.raise_for_status()  # Проверяем на наличие ошибок
        data = response.json()
        return data['content'], data['author']
    except requests.RequestException as e:
        return "Не удалось загрузить цитату. Попробуйте позже.", "API"

# Функция для перевода текста на русский язык
def translate_to_russian(text):
    try:
        translator = Translator(to_lang="ru")
        translation = translator.translate(text)
        return translation
    except Exception:
        return "Ошибка перевода"


@app.route("/")
def index():
    quote, author = get_random_quote()
    translated_quote = translate_to_russian(quote)
    return render_template("index.html", quote=quote, author=author, translated_quote=translated_quote)

if __name__ == '__main__':
    app.run(debug=True)
