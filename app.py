from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import logging
from datetime import datetime

# 1. Лог жүйесін реттейміз (Әрбір әрекетті "bank_server.log" деген файлға жазып отырады)
logging.basicConfig(
    filename="bank_server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

app = FastAPI(title="Bank Churn API with Logging")
model = joblib.load("bank_model.pkl")
logging.info("Банк сервері және Жасанды Интеллект моделі сәтті іске қосылды.")

class CustomerData(BaseModel):
    credit_score: int
    age: int
    tenure: int
    balance: float
    num_products: int
    has_credit_card: int
    is_active_member: int
    estimated_salary: float

@app.get("/")
def home():
    logging.info("Басты бетке сұраныс түсті.")
    return {"message": "Банк ИИ Моделінің Сервері Қосылып Тұр!"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    try:
        # Клиент мәліметі келгенін логқа жазамыз
        logging.info(
            f"Болжамға сұраныс келді: Жасы={data.age}, Кредит Скор={data.credit_score}, Баланс={data.balance}"
        )

        input_data = np.array([[
            data.credit_score, data.age, data.tenure, data.balance,
            data.num_products, data.has_credit_card, data.is_active_member, data.estimated_salary
        ]])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        result_prob = round(float(probability) * 100, 2)

        # ИИ-дің шешімін логқа таңбалаймыз
        logging.info(f"ИИ Болжамы сәтті аяқталды: Шешім={prediction}, Ықтималдық={result_prob}%")

        return {
            "churn_prediction": int(prediction),
            "churn_probability": result_prob
        }
    except Exception as e:
        # Егер кодта кенеттен қате кетсе, оны логқа ҚАТЕ деп жазады
        logging.error(
            f"Болжам жасау кезінде техникалық ҚАТЕ кетті: {str(e)}",
            exc_info=True
        )
        return {"error": "Сервер ішінде қате пайда болды"}
