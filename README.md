#  AI Workout Planner

An AI-powered web app built with **Streamlit** and **LangChain**, using **Groq’s LLaMA-3** model to generate personalized weekly workout plans based on user goals, fitness level, duration, equipment, and weight.

## Features

- Custom weekly workout plan generation
- LLaMA-3 integration via Groq API
- Warm-up, main workout, cool-down & dietary tips
- Easy-to-use web interface built with Streamlit

##  Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-workout-planner.git
```

2. Create and Activate a Virtual Environment
```bash
python -m venv env
.\env\Scripts\activate 
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Set Your API Key
Create a .env file in the root directory and add your Groq API key:

GROQ_API_KEY="your_actual_groq_api_key"

5. Run the App
```bash
streamlit run app.py
```