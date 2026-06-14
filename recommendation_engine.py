from recommendation.work_recommendation import work_remedies
from recommendation.sleep_recommendation import sleep_remedies
from recommendation.emotional_recommendation import emotional_remedies
from recommendation.lifestyle_recommendation import lifestyle_remedies


def recommend_remedy(stress_level, stress_cause):

    cause_map = {

        "Work": work_remedies(),

        "Sleep": sleep_remedies(),

        "Emotional": emotional_remedies(),

        "Lifestyle": lifestyle_remedies()
    }

    return cause_map[stress_cause][stress_level]

def generate_daily_plan(recommendations):

    plan = []
    total_time = 0

    for category in recommendations.values():

        for activity in category:

            plan.append(
                f"{activity['name']} "
                f"({activity['time_min']} min)"
            )

            total_time += activity["time_min"]

    return {
        "activities": plan,
        "total_time": total_time
    }