from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()  # Charge les variables depuis .env

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

valid_langs = {"EN", "FR", "ES","ZH","RU"}  # majuscules car DeepL attend ça

@app.route("/", methods=["GET", "POST"])
def index():
    translation = ""
    text_to_translate = ""
    target_lang = "EN"  # valeur par défaut

    if request.method == "POST":
        text_to_translate = request.form.get("text_to_translate", "").strip()
        target_lang = request.form.get("target_lang", "EN").upper()

        if not text_to_translate:
            translation = "⚠️ Veuillez entrer un texte à traduire."
        elif target_lang not in valid_langs:
            translation = "⚠️ Langue cible non supportée."
        else:
            try:
                response = requests.post(
                    DEEPL_API_URL,
                    data={
                        "auth_key": DEEPL_API_KEY,
                        "text": text_to_translate,
                        "target_lang": target_lang,
                    },
                    timeout=10
                )
                response.raise_for_status()
                result = response.json()
                translation = result["translations"][0]["text"]
            except Exception as e:
                translation = f"Erreur lors de la traduction : {str(e)}"

    return render_template(
        "index.html",
        translation=translation,
        text_to_translate=text_to_translate,
        target_lang=target_lang,
    )


if __name__ == "__main__":
    app.run(debug=True)
