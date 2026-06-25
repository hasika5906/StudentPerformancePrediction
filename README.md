# 🎓 Student Performance Prediction System

## 📖 Project Overview

The Student Performance Prediction System is a Machine Learning-based web application developed to analyze student academic performance and predict grades using various academic, behavioral, and demographic factors.

The system helps students, educators, and institutions identify academic strengths, weaknesses, risk factors, and improvement opportunities through intelligent prediction and visual analytics.

The application combines Machine Learning, Data Analytics, Visualization, and Web Technologies to provide meaningful academic insights and personalized recommendations.

---

# 🎯 Objectives

* Predict student academic grades using Machine Learning.
* Analyze academic strengths and weaknesses.
* Calculate Academic Health Score.
* Visualize academic performance through dynamic charts.
* Compare student performance with average and similar students.
* Provide data-driven insights for academic improvement.
* Support educational decision-making using predictive analytics.

---

# 🚀 Key Features

## 1. Student Grade Prediction

Predicts student grade based on:

* Attendance
* Midterm Score
* Final Score
* Assignments
* Quizzes
* Projects
* Study Hours
* Stress Level
* Sleep Hours
* Family and Educational Background

---

## 2. Academic Health Score

Calculates an overall academic health score out of 100 to represent the student's academic standing.

---

## 3. Strength Analysis

Identifies strong areas such as:

* Excellent Attendance
* Strong Assignment Performance
* Good Project Work
* Good Quiz Performance

---

## 4. Weakness Analysis

Detects areas needing improvement such as:

* Low Attendance
* Poor Study Habits
* High Stress Levels
* Insufficient Sleep

---

## 5. Dynamic Visualizations

The system generates personalized charts for every student:

### Academic Profile Chart

Displays performance in:

* Attendance
* Midterm
* Final
* Assignments
* Quizzes
* Participation
* Projects

### Risk Analysis Chart

Visualizes risk factors such as:

* Attendance Risk
* Study Habit Risk
* Stress Risk
* Sleep Risk

### Student vs Average Comparison

Compares the student against dataset averages.

---

## 6. Similar Student Analysis

Uses K-Nearest Neighbors (KNN) algorithm to identify students with similar academic characteristics.

---

## 7. Comparison Dashboard

Allows comparison with:

* Average Student
* Similar Students
* High Performing Students

---

## 8. About Project Page

Provides:

* Project Information
* Technology Stack
* Dataset Details
* Machine Learning Details

---

# 🛠 Technology Stack

## Frontend

* HTML5
* CSS3

## Backend

* Python
* Flask

## Machine Learning

* Scikit-Learn
* Random Forest Classifier
* K-Nearest Neighbors (KNN)

## Data Processing

* Pandas
* NumPy

## Data Visualization

* Matplotlib

## Model Serialization

* Joblib

---

# 📂 Dataset Features

The model uses the following features:

* Gender
* Age
* Department
* Attendance (%)
* Midterm Score
* Final Score
* Assignments Average
* Quizzes Average
* Participation Score
* Projects Score
* Study Hours Per Week
* Extracurricular Activities
* Internet Access At Home
* Parent Education Level
* Family Income Level
* Stress Level
* Sleep Hours Per Night

Target Variable:

* Grade

---

# 🤖 Machine Learning Model

## Random Forest Classifier

The Random Forest Classifier was selected because:

* Handles mixed feature types efficiently.
* Reduces overfitting.
* Provides high prediction accuracy.
* Generates feature importance scores.
* Works well on educational datasets.

---

# 📊 Feature Importance

Top influential factors identified by the model:

| Rank | Feature             |
| ---- | ------------------- |
| 1    | Final Score         |
| 2    | Projects Score      |
| 3    | Midterm Score       |
| 4    | Assignments Average |
| 5    | Participation Score |

These factors contribute the most toward grade prediction.

---

# 🏗 System Architecture

Student Input

↓

Data Preprocessing

↓

Feature Encoding

↓

Machine Learning Model

↓

Grade Prediction

↓

Performance Analysis

↓

Visualization Dashboard

↓

Recommendations

---

# 📁 Project Structure

StudentPerformancePrediction/

├── backend/

│ └── app.py

│

├── frontend/

│ ├── templates/

│ │ ├── index.html

│ │ ├── result.html

│ │ ├── comparison.html

│ │ └── about.html

│ │

│ └── static/

│ ├── style.css

│ ├── student_profile.png

│ ├── risk_profile.png

│ └── comparison_chart.png

│

├── dataset/

│ └── Students Performance Dataset.csv

│

├── models/

│ ├── student_performance_model.pkl

│ └── label_encoders.pkl

│

├── screenshots/

│

├── README.md

│

└── requirements.txt

---

# ⚙️ Installation Guide

## Step 1: Download Project

Clone the repository:

git clone <repository-url>

OR

Download the ZIP file and extract it.

---

## Step 2: Open Project Folder

Navigate to project folder:

cd StudentPerformancePrediction

---

## Step 3: Create Virtual Environment

Windows:

python -m venv venv

---

## Step 4: Activate Virtual Environment

Windows:

venv\Scripts\activate

You should see:

(venv)

at the beginning of the terminal.

---

## Step 5: Install Required Packages

pip install -r requirements.txt

Wait until all packages are installed successfully.

---

## Step 6: Verify Files

Ensure these files exist:

models/student_performance_model.pkl

models/label_encoders.pkl

dataset/Students Performance Dataset.csv

---

## Step 7: Run Application

Navigate to backend folder:

cd backend

Run:

python app.py

You should see:

* Running on http://127.0.0.1:5000

---

## Step 8: Open Browser

Open:

http://127.0.0.1:5000

The application will start successfully.

---

# 🖥 Application Workflow

Home Page

↓

Enter Student Details

↓

Analyze Student Performance

↓

Result Page

↓

Comparison Dashboard

↓

About Project Page

---

# 📸 Screenshots

Recommended screenshots:

1. Home Page
2. Student Input Form
3. Prediction Result Page
4. Academic Profile Chart
5. Risk Analysis Chart
6. Comparison Dashboard
7. About Project Page

Store screenshots inside:

screenshots/

folder.

---

# 🎓 Educational Applications

This project can be used for:

* Student Performance Monitoring
* Academic Risk Detection
* Educational Data Analytics
* Student Support Systems
* Academic Improvement Planning
* Educational Research

---

# 🔮 Future Enhancements

Potential future improvements:

* PDF Report Generation
* Real-Time Student Monitoring
* Cloud Deployment
* Multi-Institution Support
* Student Login System
* Advanced Analytics Dashboard

---

# 👨‍💻 Developer

Hasika

Department of Computer Science and Engineering

Sri Sairam Engineering College

Academic Year: 2025–2026

---

# 📜 License

This project is developed solely for academic and educational purposes.

No commercial use intended.

---

# 🙏 Acknowledgement

Special thanks to the faculty members, institution, and open-source community for providing guidance, datasets, tools, and technologies that supported the development of this project.
