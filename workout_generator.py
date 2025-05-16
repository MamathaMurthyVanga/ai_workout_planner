import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

def generate_workout(user_input):
    llm = ChatGroq(
        temperature=0.7,
        model_name="llama-3.3-70b-versatile",
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    prompt_template = PromptTemplate(
        input_variables=["goal", "level", "duration", "equipment", "weight"],
        template="""
        Create a detailed weekly workout plan for a person with the following details:
        - Fitness goal: {goal}
        - Fitness level: {level}
        - Workout duration per session: {duration} minutes
        - Available equipment: {equipment}
        - Weight: {weight} kg

        Include warm-up, main workout (with exercises, sets, reps), cool-down, and dietary tips.
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt_template)
    return chain.run(user_input)
