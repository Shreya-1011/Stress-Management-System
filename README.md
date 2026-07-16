# 🧠 AI-Powered Stress Management System

An end-to-end Machine Learning web application that predicts a user's stress level, identifies the primary cause of stress, and provides personalized wellness recommendations through an interactive Streamlit dashboard.

---

# 🌐 Live Demo

🚀 **Try the application here**

https://stress-management-system-2.onrender.com

> **Note:** This application is hosted on Render's free tier. The first request after a period of inactivity may take approximately **30–60 seconds** while the server wakes up.

---

# ⭐ Project Highlights

- 🤖 End-to-End Machine Learning Project
- 🌐 Interactive Streamlit Web Application
- 📊 Random Forest Classification Model
- 📈 Interactive Plotly Visualizations
- 🧠 Root Cause Analysis
- 💡 Personalized Wellness Recommendations
- 📅 Automated Daily Action Plan
- ☁️ Deployed on Render

---

# 📌 Overview

Stress is influenced by multiple lifestyle, health, and work-related factors. This project leverages Machine Learning to analyze user inputs and predict stress levels while providing meaningful insights into the underlying causes of stress.

The application enables users to:

- Predict Stress Level
- Identify Primary Stress Cause
- Analyze Contributing Stress Factors
- Receive Personalized Wellness Recommendations
- Generate a Daily Wellness Action Plan

---

# 🚀 Features

## 📊 Stress Level Prediction

Predicts user stress into one of three categories:

- 🟢 Low Stress
- 🟡 Medium Stress
- 🔴 High Stress

using a trained **Random Forest Classifier**.

---

## 🧠 Stress Cause Analysis

Determines the dominant contributor to stress among:

- 💼 Work Stress
- 😴 Sleep Issues
- 🌿 Lifestyle Habits
- ❤️ Emotional Factors

Visualized using an interactive Plotly bar chart.

---

## 💡 Personalized Recommendations

Based on the predicted stress level and primary stress cause, the application recommends activities such as:

- Meditation
- Exercise
- Sleep Improvement
- Time Management
- Digital Detox
- Social Activities

---

## 📅 Daily Action Plan

Automatically generates a practical daily wellness schedule containing:

- Recommended activities
- Estimated completion time
- Priority-based tasks

---

# 🛠️ Tech Stack

### Programming Language

- Python

### Machine Learning

- Random Forest Classifier
- Scikit-learn

### Data Processing

- Pandas
- NumPy

### Model Serialization

- Joblib

### Data Visualization

- Plotly

### Web Framework

- Streamlit

### Deployment

- Render

---

# 📂 Project Structure

```text
Stress-Management-System/
│
├── app.py
├── recommendation_engine.py
├── StressCauses.py
│
├── Models/
│   └── Random_Forest.pkl
│
├── Dataset/
├── requirements.txt
├── README.md
└── runtime.txt
```

---

# 📊 Input Features

The model predicts stress using the following features:

| Feature | Description |
|----------|-------------|
| Age | Your age |
| Sleep Duration | Average hours of sleep each day |
| Physical Activity | Amount of daily physical exercise or movement |
| Screen Time | Hours spent using phones, laptops, or other digital devices |
| Caffeine Intake | Number of caffeinated drinks (coffee, tea, energy drinks) consumed per day |
| Alcohol Intake | Frequency of alcohol consumption |
| Smoking Habit | Whether the person smokes or not |
| Work Hours | Average number of working or study hours each day |
| Travel Time | Daily time spent travelling to work or college |
| Social Interactions | Time spent interacting with family, friends, or colleagues |
| Meditation Practice | Whether the person practices meditation regularly |
| Blood Pressure | Blood pressure level |
| Blood Sugar | Blood sugar level |
| Cholesterol | Cholesterol level |
| Marital Status | Whether the person is married or not |


---

# ⚙️ Feature Engineering

The application generates additional features to improve prediction quality:

- Health Risk Score
- Lifestyle Risk Score
- Work-Life Balance
- Stress Exposure

These engineered features help improve the model's predictive capability.

---

# 🤖 Machine Learning Model

### Algorithm

- Random Forest Classifier

### Why Random Forest?

- Handles non-linear relationships effectively
- Performs well on tabular healthcare datasets
- Reduces overfitting through ensemble learning
- Provides strong predictive performance

---

# 📈 Prediction Classes

| Class | Meaning |
|--------|---------|
| 0 | Low Stress |
| 1 | Medium Stress |
| 2 | High Stress |

---

# 📷 Dashboard Modules

### 📍 Prediction Dashboard

Displays:

- Sleep Hours
- Work Hours
- Screen Time
- Predicted Stress Level

---

### 📍 Stress Cause Analysis

Visualizes:

- Work Stress Score
- Sleep Score
- Lifestyle Score
- Emotional Score

using an interactive Plotly chart.

---

### 📍 Personalized Recommendations

Generates:

- Wellness Recommendations
- Daily Wellness Action Plan
- Stress Management Tips

---

# 📦 Installation

### Clone the repository

```bash
git clone https://github.com/Shreya-1011/Stress-Management-System.git
```

### Move to the project directory

```bash
cd Stress-Management-System
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

# 🎯 Future Improvements

- AI-powered chatbot for stress counseling
- Stress trend tracking over time
- User authentication and profile management
- Cloud database integration
- Mobile-responsive interface

---

# 📄 License

This project is intended for educational, research, and portfolio purposes.

---

# 👩‍💻 Author

**Shreya Patel**
