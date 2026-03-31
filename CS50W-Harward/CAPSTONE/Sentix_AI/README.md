# Sentix AI Suite

## Description

Sentix AI Suite is a web application built using Django and JavaScript that allows users to perform text analysis tasks including sentiment analysis, text summarization, and keyword extraction. Users can log in, analyze text, and view their past analysis history through a dashboard.

---

## Distinctiveness and Complexity

This project is distinct from the other CS50W projects because it is not a social network, e-commerce site, or based on any previous course assignments. Instead, it is a full-stack web application focused on natural language processing (NLP) and text analytics.

The project demonstrates complexity through the integration of multiple independent systems:

- Sentiment analysis using NLTK’s VADER model to evaluate emotional tone in text.
- Extractive text summarization using a frequency-based algorithm to identify key sentences.
- Keyword extraction using the RAKE algorithm to identify important terms in a given text.
- A user authentication system allowing personalized data storage.
- A dashboard that aggregates user activity and displays statistics using Chart.js.
- A detailed view system where users can inspect individual analyses with dynamic rendering based on the type of analysis performed.

Additionally, the application uses Django models to persist user data, allowing users to track their past analyses. The frontend and backend are tightly integrated, with JSON responses enabling dynamic updates without requiring full page reloads.

This combination of machine learning techniques, data visualization, and user-specific interaction makes the project significantly more complex than typical CRUD applications and demonstrates the use of multiple technologies working together.

This project is not based on any previous CS50W assignment and was designed and implemented independently.

---

## Files and Structure

- `views.py`: Contains all backend logic including authentication, sentiment analysis, summarization, and keyword extraction.
- `models.py`: Defines the `Analyze` model used to store user analysis data for each user.
- `templates/`: Contains all HTML templates.
  - `layout.html`: Base layout with sidebar and navigation.
  - `index.html`: Dashboard page showing analytics and charts.
  - `analyze.html`: Sentiment analysis page.
  - `summarize.html`: Text summarization page.
  - `extract_keyword.html`: Keyword extraction page.
  - `details.html`: Users past data page.
- `static/`: No separate static files are used. All JavaScript is written directly inside HTML templates using `<script>` tags.
- `requirements.txt`: Lists all required Python packages.

---

## How to Run the Application

pip install -r requirements.txt
python manage.py makemigrations processor
python manage.py migrate
python manage.py runserver
Open the app in your browser:

http://127.0.0.1:8000/


---

## 🌐 Live Demo

You can view the deployed application here:

👉 https://sentix-ai-2b7w.onrender.com/

---

## Additional Information

- The project uses the NLTK VADER model for sentiment analysis.
- RAKE is used for keyword extraction.
- Chart.js is used for data visualization in the dashboard.
- All user data is stored and retrieved using Django models.

---

## Requirements

- Python 3.x
- Django
- nltk
- rake-nltk
