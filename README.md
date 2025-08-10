# Predicción de Fuga de Clientes (Customer Churn Prediction Pipeline)

## Descripción
Este proyecto implementa un pipeline completo para predecir la probabilidad de que un cliente cancele un servicio (fuga o churn). Incluye un proceso ETL para limpiar y transformar datos, un modelo de Machine Learning entrenado con XGBoost, una API REST con FastAPI para predicciones y un dashboard con Streamlit para visualización interactiva.

## Tecnologías usadas
- Python 3.10+
- Pandas, Scikit-learn, XGBoost
- FastAPI, Uvicorn
- Streamlit

## Estructura del proyecto
customer_churn_project/
│── data/
│ ├── raw/ # Dataset original
│ ├── processed/ # Datos limpios
│── src/
│ ├── etl.py # Script ETL (extract, transform, load)
│ ├── train.py # Entrenamiento de modelo
│── models/
│ └── churn_model.pkl # Modelo guardado
│── app/
│ ├── api.py # API FastAPI para predicción
│ ├── dashboard.py # Dashboard Streamlit
│── requirements.txt
│── README.md

## Cómo usarlo

### 1. Configurar entorno
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 2. Preparar datos

Coloca el archivo WA_Fn-UseC_-Telco-Customer-Churn.csv en data/raw/.

Ejecuta el pipeline ETL:
python src/etl.py


### 3. Entrenar el modelo
mkdir models
python src/train.py

### 4. Ejecutar API para predicción

uvicorn app.api:app --reload


### 5. Ejecutar dashboard
streamlit run app/dashboard.py


### Uso de la API

Envia un POST a http://localhost:8000/predict con un JSON con las características del cliente.
{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "MultipleLines": "No",
  "InternetService": "Fiber optic",
  "OnlineSecurity": "No",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "StreamingTV": "No",
  "StreamingMovies": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Electronic check",
  "MonthlyCharges": 70.35,
  "TotalCharges": 1397.475
}
