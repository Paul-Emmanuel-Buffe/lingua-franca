from flask import Flask, render_template, request, jsonify  # Import Flask and tools for web rendering and AJAX
import requests  # Used to make HTTP requests
import os  # Used to access environment variables
from dotenv import load_dotenv  # Used to load variables from a .env file


class TranslationService:
    # This class manages the translation logic
    
    def __init__(self, api_key, api_url):
        # Initialize with API credentials and a set of allowed languages
        self.api_key = api_key
        self.api_url = api_url
        self.valid_langs = {"EN", "FR", "ES", "ZH", "RU"}  # Supported languages

    def is_valid_language(self, lang):
        # Check if the selected language is supported
        return lang in self.valid_langs

    def translate(self, text, target_lang):
        # Handle the translation logic

        if not text:
            return "", "Please enter text to translate."  # Error if no input
        
        if not self.is_valid_language(target_lang):
            return "",  "Target language not supported."  # Error if unsupported language
        
        try:
            # Send translation request to DeepL API
            response = requests.post(
                self.api_url,
                data={
                    "auth_key": self.api_key,
                    "text": text,
                    "target_lang": target_lang,
                },
                timeout=10
            )
            response.raise_for_status()  # Raise an error if the request failed
            result = response.json()  # Parse the JSON response
            translation = result["translations"][0]["text"]  # Extract the translated text
            return translation, None
        except Exception as e:
            return "", f"Translation error: {str(e)}"  # Handle request/response errors


class TranslatorApp:
    # This class sets up the Flask web application
    
    def __init__(self):
        self.app = Flask(__name__)  # Create Flask app
        load_dotenv()  # Load environment variables from .env file
        self.translation_service = TranslationService(
            api_key=os.getenv("DEEPL_API_KEY"),  # Get API key from .env
            api_url="https://api-free.deepl.com/v2/translate"  # DeepL free API endpoint
        )
        self.setup_routes()  # Define app routes

    def setup_routes(self):
        # Define all routes of the app

        @self.app.route("/")
        def index():
            return render_template("index.html")  # Render main HTML page

        @self.app.route("/translate_ajax", methods=["POST"])
        def translate_ajax():
            # Handle AJAX request for translation
            text_to_translate = request.form.get("text_to_translate", "").strip()
            target_lang = request.form.get("target_lang", "EN").upper()
            translation, error = self.translation_service.translate(text_to_translate, target_lang)
            return jsonify({
                "success": error is None,
                "translation": translation if not error else error
            })

    def run(self, debug=True):
        # Run the web app in debug mode
        self.app.run(debug=debug)


# Application entry point
if __name__ == "__main__":
    # Start the app if the script is run directly
    translator_app = TranslatorApp()
    translator_app.run(debug=True)
