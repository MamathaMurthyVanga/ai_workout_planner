# import streamlit as st
# from workout_generator import generate_workout
# from pdf_generator import generate_pdf

# st.title("🏋️ AI Workout Planner")

# with st.form("Workout Planner"):
#     goal = st.selectbox("Fitness Goal", ["Muscle Gain", "Weight Loss", "Endurance", "Flexibility"])
#     level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
#     duration = st.slider("Workout Duration (minutes)", 15, 90, 45)
#     equipment = st.text_input("Available Equipment", "Dumbbells, Yoga Mat")
#     weight = st.number_input("Your Weight (kg)", min_value=30, max_value=200, step=1)
#     submitted = st.form_submit_button("Generate Workout Plan")

# if submitted:
#     st.info("Generating your plan...")
#     user_input = {
#         "goal": goal,
#         "level": level,
#         "duration": duration,
#         "equipment": equipment,
#         "weight": weight
#     }

#     workout_plan = generate_workout(user_input)
#     st.success("Plan Generated!")
#     st.text_area("Your Workout Plan", workout_plan, height=300)

#     if st.button("Download PDF"):
#         generate_pdf(workout_plan)
#         with open("Workout_Plan.pdf", "rb") as f:
#             st.download_button("Download Your Plan", f, file_name="Workout_Plan.pdf")



import streamlit as st
from workout_generator import generate_workout

st.set_page_config(page_title="AI Workout Planner", layout="wide")

st.markdown("<h1 style='text-align: center; color: #4B6EAF;'>🏋️‍♀️ AI Workout Planner</h1>", unsafe_allow_html=True)
# st.markdown("---")


# Use columns with some padding and subtle background
left_col, right_col = st.columns([1, 2], gap="large")

with left_col:
    st.markdown("<h3 style='color: #2E4057;'>Your Workout Preferences</h3>", unsafe_allow_html=True)
    st.write("Fill out the details below to generate a personalized workout plan.")
    
    st.write("")  # spacer
    goal = st.selectbox("Fitness Goal", ["Lose weight", "Build muscle", "Improve endurance", "Stay active"])
    level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
    duration = st.slider("Workout Duration (minutes)", 15, 120, 45)
    equipment = st.text_input("Available Equipment (comma separated)", "Dumbbells, Yoga Mat")
    weight = st.number_input("Weight (kg)", 30, 200, 70)
    generate_btn = st.button("Generate Workout Plan", key="generate")

with right_col:
    st.markdown("<h3 style='color: #2E4057;'>Your Personalized Plan</h3>", unsafe_allow_html=True)

    if generate_btn:
        with st.spinner("Creating your workout plan..."):
            try:
                user_input = {
                    "goal": goal,
                    "level": level,
                    "duration": duration,
                    "equipment": equipment,
                    "weight": weight
                }
                workout_plan = generate_workout(user_input)
                st.success("Here is your plan!")
                st.markdown(workout_plan)
            except Exception as e:
                st.error(f"Oops! Something went wrong:\n{e}")
    else:
        st.info("Enter your details on the left and click 'Generate Workout Plan'.")

# Optional: add footer or branding
# st.markdown("---")
# st.markdown("<p style='text-align: center; font-size: 12px; color: #888;'>Built with ❤️ using LangChain and Streamlit</p>", unsafe_allow_html=True)
