import joblib
import pandas as pd

# Load model
model = joblib.load(
    "../models/student_performance_model.pkl"
)

# Load encoders
label_encoders = joblib.load(
    "../models/label_encoders.pkl"
)

# Sample Student

sample = {
    "Gender": "Female",
    "Age": 20,
    "Department": "CS",
    "Attendance (%)": 95,
    "Midterm_Score": 88,
    "Final_Score": 92,
    "Assignments_Avg": 90,
    "Quizzes_Avg": 85,
    "Participation_Score": 80,
    "Projects_Score": 90,
    "Study_Hours_per_Week": 25,
    "Extracurricular_Activities": "Yes",
    "Internet_Access_at_Home": "Yes",
    "Parent_Education_Level": "Master's",
    "Family_Income_Level": "High",
    "Stress_Level (1-10)": 3,
    "Sleep_Hours_per_Night": 8
}

df = pd.DataFrame([sample])

# Encode categorical columns

for col in label_encoders:

    if col != "Grade":

        df[col] = label_encoders[col].transform(
            df[col]
        )

# Predict

prediction = model.predict(df)[0]

grade = label_encoders[
    "Grade"
].inverse_transform(
    [prediction]
)[0]

print("\nPredicted Grade:", grade)