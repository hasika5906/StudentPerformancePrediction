from flask import Flask, render_template, request
import pandas as pd
import joblib
from sklearn.neighbors import NearestNeighbors
from flask import redirect
import matplotlib.pyplot as plt

latest_result = {}
app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# =====================================
# LOAD MODEL
# =====================================

model = joblib.load(
    "../models/student_performance_model.pkl"
)

label_encoders = joblib.load(
    "../models/label_encoders.pkl"
)

# =====================================
# LOAD DATASET
# =====================================

dataset = pd.read_csv(
    "../dataset/Students Performance Dataset.csv"
)

# =====================================
# GLOBAL STORAGE
# =====================================

latest_student = {}
latest_report = {}
# =====================================
# HOME
# =====================================

@app.route("/")
def home():
    return render_template("index.html")

# =====================================
# PREDICT
# =====================================

@app.route("/predict", methods=["POST"])
def predict():

    global latest_student
    global latest_report

    data = {
        "Gender": request.form["Gender"],
        "Age": int(request.form["Age"]),
        "Department": request.form["Department"],
        "Attendance (%)": float(request.form["Attendance"]),
        "Midterm_Score": float(request.form["Midterm"]),
        "Final_Score": float(request.form["Final"]),
        "Assignments_Avg": float(request.form["Assignments"]),
        "Quizzes_Avg": float(request.form["Quizzes"]),
        "Participation_Score": float(request.form["Participation"]),
        "Projects_Score": float(request.form["Projects"]),
        "Study_Hours_per_Week": float(request.form["StudyHours"]),
        "Extracurricular_Activities": request.form["Extra"],
        "Internet_Access_at_Home": request.form["Internet"],
        "Parent_Education_Level": request.form["ParentEdu"],
        "Family_Income_Level": request.form["Income"],
        "Stress_Level (1-10)": int(request.form["Stress"]),
        "Sleep_Hours_per_Night": float(request.form["Sleep"])
    }

    latest_student = data.copy()

    df = pd.DataFrame([data])

    for col in label_encoders:
        if col != "Grade":
            df[col] = label_encoders[col].transform(df[col])

    prediction = model.predict(df)[0]

    grade = label_encoders["Grade"].inverse_transform(
        [prediction]
    )[0]

    attendance = data["Attendance (%)"]

    if attendance >= 80:
        risk = "Low Risk"
    elif attendance >= 60:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    health_score = round(
        (
            data["Attendance (%)"]
            + data["Assignments_Avg"]
            + data["Quizzes_Avg"]
            + data["Projects_Score"]
            + data["Final_Score"]
        ) / 5
    )

    if health_score >= 90:
        performance_status = "Excellent"
    elif health_score >= 75:
        performance_status = "Good"
    elif health_score >= 60:
        performance_status = "Average"
    else:
        performance_status = "Needs Improvement"

    strengths = []
    weaknesses = []
    recommendations = []

    if data["Attendance (%)"] >= 85:
        strengths.append("Excellent Attendance")

    if data["Projects_Score"] >= 80:
        strengths.append("Excellent Project Work")

    if data["Assignments_Avg"] >= 80:
        strengths.append("Strong Assignment Performance")

    if data["Attendance (%)"] < 75:
        weaknesses.append("Low Attendance")

    if data["Study_Hours_per_Week"] < 15:
        weaknesses.append("Insufficient Study Hours")

    if data["Stress_Level (1-10)"] > 7:
        weaknesses.append("High Stress Level")

    if data["Midterm_Score"] < 25:
        recommendations.append(
            "Improve Midterm Preparation"
        )

    if data["Assignments_Avg"] < 60:
        recommendations.append(
            "Improve Assignment Quality"
        )

    if data["Projects_Score"] < 70:
        recommendations.append(
            "Focus On Project Development"
        )

    if data["Attendance (%)"] < 75:
        recommendations.append(
            "Improve Attendance"
        )

    avg_attendance = round(
        dataset["Attendance (%)"].mean(),
        2
    )

    avg_study_hours = round(
        dataset["Study_Hours_per_Week"].mean(),
        2
    )

    attendance_diff = round(
        data["Attendance (%)"] - avg_attendance,
        2
    )

    study_diff = round(
        data["Study_Hours_per_Week"] - avg_study_hours,
        2
    )
    # =====================================
    # CHART 1
    # ACADEMIC PROFILE
    # =====================================

    plt.figure(figsize=(8,5))

    features = [
    "Attendance",
    "Midterm",
    "Final",
    "Assignments",
    "Quizzes",
    "Projects",
    "Participation"
    ]
    values = [

    data["Attendance (%)"],

    data["Midterm_Score"] * 2,

    data["Final_Score"],

    data["Assignments_Avg"],

    data["Quizzes_Avg"],

    data["Projects_Score"],

    data["Participation_Score"]

    ]
    plt.bar(
    features,
    values
    )

    plt.title(
    "Academic Performance Profile"
    )

    plt.ylabel("Score")

    plt.tight_layout()

    plt.savefig(
    "../frontend/static/student_profile.png"
    )

    plt.close()

    # =====================================
# CHART 2
# RISK ANALYSIS
# =====================================

    attendance_risk = max(
    0,
    100 - data["Attendance (%)"]
    )

    study_risk = max(
    0,
    20 - data["Study_Hours_per_Week"]
    ) * 5

    sleep_risk = max(
    0,
    8 - data["Sleep_Hours_per_Night"]
    ) * 10

    stress_risk = (
    data["Stress_Level (1-10)"] * 10
    )

    plt.figure(figsize=(6,6))

    plt.pie(

        [
        attendance_risk,
        study_risk,
        sleep_risk,
        stress_risk
        ],

        labels=[

        "Attendance",

        "Study",

        "Sleep",

        "Stress"

        ],

        autopct="%1.1f%%"

    )

    plt.title(
    "Risk Factor Analysis"
    )

    plt.savefig(
    "../frontend/static/risk_profile.png"
    )

    plt.close()

    # =====================================
# CHART 3
# STUDENT VS AVERAGE
# =====================================

    avg_assignments = round(
    dataset["Assignments_Avg"].mean(),
    2
    )

    avg_projects = round(
    dataset["Projects_Score"].mean(),
    2
    )   

    student_values = [

    data["Attendance (%)"],

    data["Assignments_Avg"],

    data["Projects_Score"],

    data["Study_Hours_per_Week"]

    ]

    average_values = [

    avg_attendance,

    avg_assignments,

    avg_projects,

    avg_study_hours

    ]

    labels = [

    "Attendance",

    "Assignments",

    "Projects",

    "Study Hours"

    ]

    x = range(
    len(labels)
    )

    plt.figure(figsize=(8,5))

    plt.bar(
    x,
    student_values,
    width=0.4,
    label="Student" 
    )

    plt.bar(
    [i+0.4 for i in x],
    average_values,
    width=0.4,
    label="Average"
    )

    plt.xticks(
    [i+0.2 for i in x],
    labels
    )

    plt.legend()

    plt.title(
    "Student vs Average"
    )

    plt.tight_layout()

    plt.savefig(
    "../frontend/static/comparison_chart.png"
    )   

    plt.close()

    global latest_result

    latest_result = {

    "prediction": grade,

    "health_score": health_score,

    "performance_status": performance_status,

    "strengths": strengths,

    "weaknesses": weaknesses

    }

    return redirect("/result")


@app.route("/comparison")
def comparison():

    global latest_student

    if len(latest_student) == 0:

        return render_template(
            "comparison.html",
            no_data=True
        )

    avg_attendance = round(
        dataset["Attendance (%)"].mean(),
        2
    )

    avg_study = round(
        dataset["Study_Hours_per_Week"].mean(),
        2
    )

    top_students = dataset[
        dataset["Grade"] == "A"
    ]

    top_attendance = round(
        top_students["Attendance (%)"].mean(),
        2
    )

    top_study = round(
        top_students["Study_Hours_per_Week"].mean(),
        2
    )

    features = [
        'Attendance (%)',
        'Midterm_Score',
        'Final_Score',
        'Assignments_Avg',
        'Projects_Score',
        'Study_Hours_per_Week'
    ]

    X = dataset[features]

    knn = NearestNeighbors(
        n_neighbors=5
    )

    knn.fit(X)

    student_vector = pd.DataFrame([{
    "Attendance (%)":
        latest_student["Attendance (%)"],

    "Midterm_Score":
        latest_student["Midterm_Score"],

    "Final_Score":
        latest_student["Final_Score"],

    "Assignments_Avg":
        latest_student["Assignments_Avg"],

    "Projects_Score":
        latest_student["Projects_Score"],

    "Study_Hours_per_Week":
        latest_student["Study_Hours_per_Week"]
}])
    

    distances, indices = knn.kneighbors(
        student_vector
    )

    similar_students = dataset.iloc[
        indices[0]
    ][
        [
            "Attendance (%)",
            "Study_Hours_per_Week",
            "Grade"
        ]
    ].to_dict(
        orient="records"
    )
    # =====================================
    # SIMILAR STUDENT GRADE DISTRIBUTION
    # =====================================

    similar_df = dataset.iloc[
        indices[0]
    ]

    grade_distribution = (
        similar_df["Grade"]
        .value_counts()
        .to_dict()
    )

    most_common_grade = (
        similar_df["Grade"]
        .mode()[0]
    )

    # =====================================
    # PLACEMENT READINESS
    # =====================================

    placement_score = round(

        (
            latest_student["Attendance (%)"] * 0.30
            + latest_student["Projects_Score"] * 0.35
            + latest_student["Participation_Score"] * 0.20
            + latest_student["Study_Hours_per_Week"] * 2.5
        )

    )

    placement_score = min(
        placement_score,
        100
    )

    if placement_score >= 80:
        placement_status = "Highly Ready"

    elif placement_score >= 60:
        placement_status = "Moderately Ready"

    else:
        placement_status = "Needs Improvement"

    # =====================================
    # SCHOLARSHIP ELIGIBILITY
    # =====================================

    if (
        latest_student["Attendance (%)"] >= 85
        and most_common_grade == "A"
    ):

        scholarship_status = "Eligible"

    elif latest_student["Attendance (%)"] >= 75:

        scholarship_status = "Likely Eligible"

    else:

        scholarship_status = "Not Eligible"

    # =====================================
    # IMPROVEMENT POTENTIAL
    # =====================================

    improvement_score = 100 - round(

        (
            latest_student["Final_Score"]
            + latest_student["Projects_Score"]
            + latest_student["Assignments_Avg"]
            + latest_student["Attendance (%)"]
        ) / 4

    )
    # =====================================
    # GOAL BASED GRADE SIMULATOR
    # =====================================

    current_grade = most_common_grade

    if current_grade == "A":

        target_attendance = latest_student["Attendance (%)"]
        target_study = latest_student["Study_Hours_per_Week"]
        target_midterm = latest_student["Midterm_Score"]

    elif current_grade == "B":

        target_attendance = 85
        target_study = 18
        target_midterm = 40

    elif current_grade == "C":

        target_attendance = 88
        target_study = 20
        target_midterm = 42

    else:

        target_attendance = 90
        target_study = 22
        target_midterm = 45

    # =====================================
    # RETURN
    # =====================================

    return render_template(

    "comparison.html",

    avg_attendance=avg_attendance,
    avg_study=avg_study,

    student_attendance=latest_student["Attendance (%)"],
    student_study=latest_student["Study_Hours_per_Week"],

    top_attendance=top_attendance,
    top_study=top_study,

    improvement_score=improvement_score,

    similar_students=similar_students,

    grade_distribution=grade_distribution,

    most_common_grade=most_common_grade,

    placement_score=placement_score,
    placement_status=placement_status,

    scholarship_status=scholarship_status,

    current_grade=current_grade,

    target_attendance=target_attendance,

    target_study=target_study,

    target_midterm=target_midterm

    )
@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


@app.route("/result")
def result():

    global latest_result

    if len(latest_result) == 0:

        return redirect("/")

    return render_template(

        "result.html",

        prediction=latest_result["prediction"],

        health_score=latest_result["health_score"],

        performance_status=latest_result["performance_status"],

        strengths=latest_result["strengths"],

        weaknesses=latest_result["weaknesses"]

    )


if __name__ == "__main__":
    app.run(debug=True)