# 🧠 AI-Powered Stress Management System

An end-to-end Machine Learning project that predicts a user's stress level, identifies the major cause of stress, and provides personalized wellness recommendations through an interactive Streamlit dashboard.

---

## 📌 Overview

Stress is influenced by multiple lifestyle, health, and work-related factors. This project uses Machine Learning to analyze user inputs and predict stress levels while also providing explainable insights and personalized recommendations.

The application allows users to:

- Predict Stress Level
- Identify Primary Stress Cause
- View Stress Cause Analysis
- Receive Personalized Wellness Recommendations
- Generate a Daily Action Plan

---

# 🚀 Features

### 📊 Stress Prediction
Predicts the user's stress level as:

- Low
- Medium
- High

using a trained Random Forest Machine Learning model.

---

### 🧠 Cause Analysis

Identifies the dominant reason behind stress among:

- Work Stress
- Sleep Issues
- Lifestyle Habits
- Emotional Factors

Displays scores using an interactive Plotly horizontal bar chart.

---

### 💡 Personalized Recommendations

Based on the predicted stress level and root cause, the system recommends activities such as:

- Meditation
- Exercise
- Sleep Improvement
- Time Management
- Digital Detox
- Social Activities

---

### 📅 Daily Action Plan

Automatically creates a practical daily wellness schedule including:

- Recommended activities
- Estimated total time
- Priority-based actions

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Machine Learning

- Random Forest Classifier
- Scikit-learn

## Data Processing

- Pandas
- NumPy

## Model Serialization

- Joblib

## Data Visualization

- Plotly Express

## Web Framework

- Streamlit

---

# 📂 Project Structure

```
Stress-Management-System/
│
├── app.py
├── recommendation_engine.py
├── StressCauses.py
│
├── Models/
│   └── Random_Forest.pkl
│
├── requirements.txt
├── README.md
└── Dataset/
```

---

# 📊 Input Features

The model uses the following user inputs:

| Feature | Description |
|----------|-------------|
| Age | User age |
| Sleep Duration | Daily sleep hours |
| Physical Activity | Activity level |
| Screen Time | Daily screen usage |
| Caffeine Intake | Daily caffeine consumption |
| Alcohol Intake | Alcohol frequency |
| Smoking Habit | Smoking status |
| Work Hours | Daily working hours |
| Travel Time | Daily commute |
| Social Interactions | Interaction score |
| Meditation Practice | Yes/No |
| Blood Pressure | Blood pressure |
| Blood Sugar | Blood sugar level |
| Cholesterol | Cholesterol level |
| Marital Status | Married/Not Married |

---

# ⚙️ Engineered Features

The application also creates additional features before prediction:

- Health Risk Score
- Lifestyle Risk Score
- Work Life Balance
- Stress Exposure

These engineered features improve prediction performance.

---

# 🤖 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Reasons for selection:

- Handles non-linear relationships
- Works well with tabular healthcare data
- Robust against overfitting
- Provides strong predictive performance

---

# 📈 Prediction Classes

| Class | Meaning |
|---------|----------|
| 0 | Low Stress |
| 1 | Medium Stress |
| 2 | High Stress |

---

# 📷 Dashboard Sections

## 1️⃣ Prediction

Displays:

- Sleep Hours
- Work Hours
- Screen Time
- Predicted Stress Level

---

## 2️⃣ Cause Analysis

Shows:

- Work Score
- Sleep Score
- Lifestyle Score
- Emotional Score

Visualized using an interactive Plotly bar chart.

---

## 3️⃣ Recommendations

Generates personalized wellness suggestions based on:

- Predicted Stress Level
- Root Cause

Also creates a daily action plan.

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/Shreya-1011/Stress-Management-System.git
```

Move into the project directory

```bash
cd Stress-Management-System
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---
