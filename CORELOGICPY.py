# Core Logic Module for Study Planner

import json
import os

def generate_schedule(subjects, total_hours, num_days):
    schedule = []
    try:
        hours_per_subject = total_hours / len(subjects)
        for day in range(1, num_days + 1):
            daily_schedule = {"Day": day, "Subjects": []}
            for subject in subjects:
                daily_schedule["Subjects"].append({
                    "Subject": subject,
                    "Hours": round(hours_per_subject, 2)
                })
            schedule.append(daily_schedule)
        return schedule
    except ZeroDivisionError:
        print("Error: No subjects provided.")
        return []


def save_schedule(schedule, filename="study_schedule.json"):
    if not schedule:
        print("Error: No schedule to save.")
        return
    with open(filename, 'w') as file:
        json.dump(schedule, file, indent=4)


def load_schedule(filename="study_schedule.json"):
    if not os.path.exists(filename):
        print(f"Error: No schedule file found at '{filename}'")
        return None
    with open(filename, 'r') as file:
        return json.load(file)


def delete_schedule(filename="study_schedule.json"):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(f"Error: No schedule file found to delete.")
