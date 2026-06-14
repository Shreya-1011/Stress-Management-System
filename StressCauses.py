# ==========================================
# STRESS CAUSE IDENTIFICATION MODULE
# ==========================================

def identify_stress_cause(user_data):

    scores = {
        "Work": 0,
        "Sleep": 0,
        "Emotional": 0,
        "Lifestyle": 0
    }

    # ======================================
    # WORK STRESS
    # ======================================

    if user_data["Work_Hours"] >= 8:
        scores["Work"] += 3

    if user_data["Travel_Time"] >= 2:
        scores["Work"] += 2

    if user_data["Screen_Time"] >= 8:
        scores["Work"] += 1

    if user_data["Work_Hours"] >= 10:
        scores["Work"] += 2

    # ======================================
    # SLEEP STRESS
    # ======================================

    if user_data["Sleep_Duration"] < 6:
        scores["Sleep"] += 4

    elif user_data["Sleep_Duration"] < 7:
        scores["Sleep"] += 2

    if user_data["Screen_Time"] >= 8:
        scores["Sleep"] += 2

    if user_data["Meditation_Practice"] == 0:
        scores["Sleep"] += 1

    # ======================================
    # EMOTIONAL STRESS
    # ======================================

    if user_data["Social_Interactions"] <= 2:
        scores["Emotional"] += 4

    elif user_data["Social_Interactions"] <= 4:
        scores["Emotional"] += 2

    if user_data["Meditation_Practice"] == 0:
        scores["Emotional"] += 1

    if user_data["Marital_Status_Married"] == 0:
        scores["Emotional"] += 1

    # ======================================
    # LIFESTYLE STRESS
    # ======================================

    if user_data["Physical_Activity"] <= 2:
        scores["Lifestyle"] += 3

    if user_data["Smoking_Habit"] == 1:
        scores["Lifestyle"] += 2

    if user_data["Alcohol_Intake"] >= 3:
        scores["Lifestyle"] += 2

    if user_data["Caffeine_Intake"] >= 4:
        scores["Lifestyle"] += 1

    # ======================================
    # FIND PRIMARY CAUSE
    # ======================================

    primary_cause = max(
        scores,
        key=scores.get
    )

    return primary_cause, scores


# ==========================================
# CAUSE EXPLANATION MODULE
# ==========================================

def explain_cause(cause):

    cause_info = {

        "Work": {
            "title": "Work Related Stress",
            "description":
            "Stress caused by workload, deadlines, commuting time and excessive screen exposure."
        },

        "Sleep": {
            "title": "Sleep Related Stress",
            "description":
            "Stress caused by insufficient sleep, excessive screen time and poor recovery."
        },

        "Emotional": {
            "title": "Emotional Stress",
            "description":
            "Stress caused by loneliness, reduced social interactions and emotional challenges."
        },

        "Lifestyle": {
            "title": "Lifestyle Related Stress",
            "description":
            "Stress caused by unhealthy habits, low physical activity and poor lifestyle choices."
        }
    }

    return cause_info[cause]


# ==========================================
# DETAILED REASON GENERATOR
# ==========================================

def generate_reasons(user_data):

    reasons = []

    if user_data["Sleep_Duration"] < 6:
        reasons.append(
            "Sleep duration is below the recommended level."
        )

    if user_data["Screen_Time"] >= 8:
        reasons.append(
            "High screen time may contribute to mental fatigue."
        )

    if user_data["Work_Hours"] >= 8:
        reasons.append(
            "Long working hours increase stress exposure."
        )

    if user_data["Travel_Time"] >= 2:
        reasons.append(
            "Long commuting time may increase stress."
        )

    if user_data["Physical_Activity"] <= 2:
        reasons.append(
            "Low physical activity may negatively affect mental health."
        )

    if user_data["Social_Interactions"] <= 2:
        reasons.append(
            "Low social interaction can increase emotional stress."
        )

    if user_data["Meditation_Practice"] == 0:
        reasons.append(
            "Lack of meditation may reduce stress resilience."
        )

    if user_data["Smoking_Habit"] == 1:
        reasons.append(
            "Smoking habit may contribute to stress and health risks."
        )

    return reasons
