from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv


class TranslationService:
    # Handles translation service with DeepL
    
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.valid_langs = {"EN", "FR", "ES", "ZH", "RU"}
        
    def is_valid_language(self, lang):
        # Checks if target language is valid
        return lang in self.valid_langs
        
    def translate(self, text, target_lang):
        # Translates text via DeepL API
        if not text:
            return "", "Please enter text to translate."
            
        if not self.is_valid_language(target_lang):
            return "",  "Target language not supported."
        
        try:
            response = requests.post(
                self.api_url,
                data={
                    "auth_key": self.api_key,
                    "text": text,
                    "target_lang": target_lang,
                },
                timeout=10
            )
            response.raise_for_status()
            result = response.json()
            translation = result["translations"][0]["text"]
            return translation, None
        except Exception as e:
            return "", f"Translation error: {str(e)}"


class TranslatorApp:
    def __init__(self):
        self.app = Flask(__name__)
        load_dotenv()
        self.translation_service = TranslationService(
            api_key=os.getenv("DEEPL_API_KEY"),
            api_url="https://api-free.deepl.com/v2/translate"
        )
        self.setup_routes()

    def setup_routes(self):
        @self.app.route("/")
        def index():
            return render_template("index.html")  # Template seul sans logique
        
        @self.app.route("/translate_ajax", methods=["POST"])
        def translate_ajax():
            text_to_translate = request.form.get("text_to_translate", "").strip()
            target_lang = request.form.get("target_lang", "EN").upper()
            translation, error = self.translation_service.translate(text_to_translate, target_lang)
            return jsonify({
                "success": error is None,
                "translation": translation if not error else error
            })

    def run(self, debug=True):
        self.app.run(debug=debug)


# Application entry point
if __name__ == "__main__":
    translator_app = TranslatorApp()
    translator_app.run(debug=True)