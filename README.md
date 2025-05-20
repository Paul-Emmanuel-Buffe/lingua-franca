# Lingua Franca

<img src="/static/img/result.png" alt="Lingua Franca Banner">
## Overview

Lingua Franca is a simple yet powerful text translation web application built with Flask. It provides users with an intuitive interface to translate text between multiple languages using Google's Translation API. Whether you need to translate a quick phrase or a longer paragraph, Lingua Franca offers a clean, straightforward solution for breaking down language barriers.

## Features

- **Text Translation**: Translate text between numerous languages supported by Google Translate API
- **Automatic Language Detection**: Don't know the source language? Let our application detect it automatically
- **Clean User Interface**: Minimalist design focused on functionality and ease of use
- **Responsive Layout**: Works well on both desktop and mobile devices

## Technologies Used

- **Python**: Core programming language
- **Flask**: Web framework for building the application
- **Google Translate API**: Provides translation capabilities
- **HTML/CSS**: Front-end structure and styling

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Conda (for environment management)

### Setting Up the Environment

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/lingua-franca.git
   cd lingua-franca
   ```

2. Create and activate a Conda environment:
   ```
   conda create --name lingua-franca python=3.9
   conda activate lingua-franca
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Configuration

1. You will need to set up access to Google Translate API:
   - Follow the [official Google Cloud documentation](https://cloud.google.com/translate/docs/setup) to create an account and obtain an API key
   - Create a `.env` file in the project root and add your API key:
     ```
     GOOGLE_TRANSLATE_API_KEY=your_api_key_here
     ```

### Running the Application

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage

1. Enter the text you wish to translate in the left text area
2. Select the source language (or choose "Auto-detect")
3. Select the target language
4. Click the "Translate" button
5. View the translated text in the right text area

## Project Structure

```
lingua-franca/
├── app.py                  # Main Flask application
├── static/                 # Static files
│   ├── css/                # CSS stylesheets
│   └── img/                # Images
├── templates/              # HTML templates
│   ├── index.html          # Main page template
│   └── layout.html         # Base layout template
├── translations/           # Translation service
│   └── google_translate.py # Google Translate API integration
├── .env                    # Environment variables (not tracked by Git)
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Limitations

- Free tier of Google Translate API has usage limits
- Some rare languages might have less accurate translations
- Performance depends on Google Translate API response time

## Contributors

- [Paul-Emmanuel Buffe](https://github.com/Paul-Emmanuel-Buffe)
- [Khady Ndiaye](https://github.com/khady-ndiaye)

## License

This project is created as an academic assignment for La Plateforme's Bachelor program. 

---

*This project was developed as part of the curriculum for Bachelor 1st year at La Plateforme.*
