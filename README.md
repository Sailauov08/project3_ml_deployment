# 🏦 Bank Customer Churn Prediction & ML Deployment

This project demonstrates a complete **End-to-End Machine Learning workflow**, starting from a database to model training, creating a live production-ready web server (API), and implementing an automated logging system.

---

## 🛠️ Tech Stack & Technologies Used

* **Programming Language:** Python 🐍
* **Machine Learning:** Scikit-Learn (RandomForestClassifier), Joblib, Pandas, NumPy
* **Database:** SQLite3
* **Web Framework (API):** FastAPI, Uvicorn, Pydantic
* **Version Control:** Git & GitHub

---

## ⚙️ What Was Done (Project Architecture)

1. **Database & Data Prep:** Created a fresh SQLite database (bank_data.db) containing bank customer features such as Credit Score, Age, Balance, and Activity status.
2. **Model Training:** Trained a Machine Learning model using the Random Forest algorithm to predict whether a customer will leave the bank (churn).
3. **Model Serialization:** Saved the trained brain of the AI into a structured bank_model.pkl file for production deployment.
4. **API Deployment:** Developed a modern, high-performance web server using FastAPI (app.py) to expose a /predict endpoint. It accepts real-time customer data and responds with instant AI predictions.
5. **Production Logging:** Implemented an enterprise-grade automated logging system (bank_server.log) that records every server event, incoming user request, AI decision, and runtime error for maintenance.

---

## 🚀 How to Run the Project

### 1. Start the FastAPI Web Server
Run the following command in your terminal to boot up the server with hot-reload enabled:
python -m uvicorn app:app --reload

### 2. Test the Live API
Once running, open your browser and navigate to:
* **Base URL:** http://127.0.0.1:8000
* **Interactive Swagger UI Documentation:** http://127.0.0.1:8000/docs

---

## 📊 API Response Example

When you send a customer payload, the AI analyzes it and returns a JSON response:

{
  "churn_prediction": 0,
  "churn_probability": 11.0
}

* churn_prediction: 0 means the customer is loyal and will stay with the bank.
* churn_probability: 11.0% indicates a very low risk of leaving.

---

## 📜 Logging System in Action
All operations are tracked in real-time inside bank_server.log:

2026-06-21 08:20:50,863 - INFO - Болжамға сұраныс келді: Жасы=40, Кредит Скор=650, Balance=10010000.0
2026-06-21 08:20:50,874 - INFO - ИИ Болжамы сәтті аяқталды: Шешім=0, Ықтималдық=11.0%
