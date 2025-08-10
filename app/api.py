from fastapi import FastAPI, HTTPException
import pandas as pd
import joblib
import os

app = FastAPI()

# Calcular ruta absoluta del modelo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "churn_model.pkl")

# Verificar existencia del modelo
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Modelo no encontrado en: {MODEL_PATH}")

# Cargar modelo
model = joblib.load(MODEL_PATH)

@app.post("/predict")
def predict(data: dict):
    try:
        # Crear DataFrame desde el input
        df = pd.DataFrame([data])
        df = pd.get_dummies(df)

        # Obtener features que el modelo espera
        model_features = model.get_booster().feature_names

        # Asegurar que todas las columnas estén presentes
        for col in model_features:
            if col not in df.columns:
                df[col] = 0

        # Ordenar columnas según el modelo
        df = df[model_features]

        # Predicción
        pred = model.predict(df)[0]
        return {"churn_probability": float(pred)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
