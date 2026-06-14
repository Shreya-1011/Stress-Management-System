import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

from StressCauses import (
    identify_stress_cause,
    explain_cause,
    generate_reasons
)

from recommendation_engine import (
    recommend_remedy,
    generate_daily_plan
)

model = joblib.load("Models/Random_Forest.pkl")

st.set_page_config(
    page_title="AI Stress Management System",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        180deg,
        #ffffff 0%,
        #f5fbf7 50%,
        #eef8ff 100%
    );
}

/* Title */
h1 {
    color: #2E7D32;
    text-align: center;
    font-weight: 700;
}

/* Section Headers */
h2, h3 {
    color: #1565C0;
}

/* Metric Cards */
div[data-testid="metric-container"] {
    background-color: white;
    border: 1px solid #dbeafe;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}

/* Tabs */
button[data-baseweb="tab"] {
    font-size: 18px;
    font-weight: 600;
}

/* Predict Button */
.stButton > button {
    background-color: #2196F3;
    color: white;
    border-radius: 12px;
    height: 3.2em;
    border: none;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #1976D2;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f7fbff;
}

/* Expander */
.streamlit-expanderHeader {
    font-size: 18px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
# 🧠 AI-Powered Stress Management System

Predict stress levels, identify root causes,
and receive personalized wellness recommendations.
""")

st.markdown("---")
st.sidebar.title("🧠 User Profile")
st.sidebar.markdown("---")
st.sidebar.header("Personal Information")

age = st.sidebar.slider("Age", 18, 80, 25)

sleep_duration = st.sidebar.number_input(
    "Sleep Duration (Hours)",
    min_value=1.0,
    max_value=12.0,
    value=7.0,
    step=0.5
)
physical_activity = st.sidebar.number_input(
    "Physical Activity",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)

screen_time = st.sidebar.slider(
    "Screen Time",
    0.0,
    15.0,
    5.0
)

caffeine = st.sidebar.slider(
    "Caffeine Intake",
    0,
    10,
    2
)

alcohol_map = {
    "Never": 0,
    "Rarely": 1,
    "Sometimes": 2,
    "Often": 3,
    "Very Often": 4,
    "Daily": 5
}

alcohol_label = st.sidebar.selectbox(
    "Alcohol Intake",
    list(alcohol_map.keys())
)

alcohol = alcohol_map[alcohol_label]

smoking = st.sidebar.selectbox(
    "Smoking Habit",
    ["No", "Yes"]
)

work_hours = st.sidebar.slider(
    "Work Hours",
    0,
    16,
    8
)

travel_time = st.sidebar.number_input(
    "Travel Time",
    min_value=0.0,
    max_value=5.0,
    value=1.0,
    step=0.5
)


social = st.sidebar.slider(
    "Social Interactions",
    0,
    10,
    5
)

meditation = st.sidebar.selectbox(
    "Meditation Practice",
    ["No", "Yes"]
)

married = st.sidebar.selectbox(
    "Married",
    ["No", "Yes"]
)

bp = st.sidebar.number_input(
    "Blood Pressure",
    value=120
)

blood_sugar = st.sidebar.number_input(
    "Blood Sugar",
    value=100
)

cholesterol = st.sidebar.number_input(
    "Cholesterol",
    value=180
)

if st.button("Predict Stress Level"):

    smoking_val = 1 if smoking == "Yes" else 0

    meditation_val = 1 if meditation == "Yes" else 0

    married_val = 1 if married == "Yes" else 0

    health_risk_score = (
        bp +
        blood_sugar +
        cholesterol
    )

    lifestyle_risk_score = (
        caffeine +
        alcohol +
        smoking_val
    )

    work_life_balance = (
        work_hours +
        travel_time
    )

    stress_exposure = (
        work_hours +
        travel_time +
        screen_time
    )

    input_df = pd.DataFrame([{

        "Age": age,
        "Sleep_Duration": sleep_duration,
        "Physical_Activity": physical_activity,
        "Screen_Time": screen_time,
        "Caffeine_Intake": caffeine,
        "Alcohol_Intake": alcohol,
        "Smoking_Habit": smoking_val,
        "Work_Hours": work_hours,
        "Travel_Time": travel_time,
        "Social_Interactions": social,
        "Meditation_Practice": meditation_val,
        "Blood_Pressure": bp,
        "Blood_Sugar_Level": blood_sugar,
        "Cholesterol_Level": cholesterol,
        "Marital_Status_Married": married_val,
        "Health_Risk_Score": health_risk_score,
        "Lifestyle_Risk_Score": lifestyle_risk_score,
        "Work_Life_Balance": work_life_balance,
        "Stress_Exposure": stress_exposure
    }])

    prediction = model.predict(input_df)[0]

    stress_map = {
        0: "Low",
        1: "Medium",
        2: "High"
    }

    stress_level = stress_map[prediction]

    tab1, tab2, tab3 = st.tabs([
    "📊 Prediction",
    "🧠 Cause Analysis",
    "💡 Recommendations"
    ])

    with tab1:

        st.header("📊 Stress Prediction")

        col1, col2, col3 = st.columns(3)

        col1.metric("Sleep Hours", sleep_duration)
        col2.metric("Work Hours", work_hours)
        col3.metric("Screen Time", screen_time)

        if stress_level == "Low":
            st.success(f"Predicted Stress Level: {stress_level}")

        elif stress_level == "Medium":
            st.warning(f"Predicted Stress Level: {stress_level}")

        else:
            st.error(f"Predicted Stress Level: {stress_level}")

    user_data = input_df.iloc[0].to_dict()

    cause, scores = identify_stress_cause(
            user_data
    )

    cause_info = explain_cause(cause)

    with tab2:

        # Score Cards

        st.subheader("📊 Stress Cause Scores")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "💼 Work",
            scores["Work"]
        )

        col2.metric(
            "😴 Sleep",
            scores["Sleep"]
        )

        col3.metric(
            "🏃 Lifestyle",
            scores["Lifestyle"]
        )

        col4.metric(
            "❤️ Emotional",
            scores["Emotional"]
        )

        # Bar Chart

        cause_df = pd.DataFrame({

            "Cause": [
                "Work",
                "Sleep",
                "Lifestyle",
                "Emotional"
            ],

            "Score": [
                scores["Work"],
                scores["Sleep"],
                scores["Lifestyle"],
                scores["Emotional"]
            ]
        })

        fig = px.bar(
            cause_df,
            x="Score",
            y="Cause",
            orientation="h",
            text="Score",
            title="Stress Cause Analysis"
        )

        fig.update_layout(
            yaxis_title="",
            xaxis_title="Stress Score",
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    recommendations = recommend_remedy(stress_level, cause)
    plan = generate_daily_plan(recommendations)
    with tab3:

        st.header("💡 Personalized Recommendations")

        for category, activities in recommendations.items():

            st.subheader(category)

            for activity in activities:

                st.info(
                    f"""
                    **{activity['name']}**

                    ⭐ Priority: {activity['priority']}

                    📈 Difficulty: {activity['difficulty']}

                    ⏱ Time: {activity['time_min']} min

                    🎯 Benefit:
                        {activity['benefit']}
                    """
                )

        st.subheader("📅 Today's Action Plan")

        for item in plan["activities"]:

            st.write("✅", item)

        st.metric(
            "Total Time Required",
            f"{plan['total_time']} min"
        )