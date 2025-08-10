# Predicción de Fuga de Clientes (Customer Churn Prediction Pipeline)

## Descripción

Este proyecto implementa un pipeline completo para predecir la probabilidad de que un cliente cancele un servicio (fuga o churn). Incluye un proceso ETL para limpiar y transformar datos, un modelo de Machine Learning entrenado con XGBoost, una API REST con FastAPI para predicciones y un dashboard con Streamlit para visualización interactiva.

## Tecnologías Utilizadas

- **Python 3.10+**
- **Procesamiento de datos:** Pandas, Scikit-learn, XGBoost
- **API:** FastAPI, Uvicorn
- **Dashboard:** Streamlit

## Estructura del Proyecto

```
customer_churn_project/
├── data/
│   ├── raw/              # Dataset original
│   └── processed/        # Datos limpios y transformados
├── src/
│   ├── etl.py           # Script ETL (Extract, Transform, Load)
│   └── train.py         # Entrenamiento del modelo
├── models/
│   └── churn_model.pkl  # Modelo entrenado guardado
├── app/
│   ├── api.py           # API FastAPI para predicciones
│   └── dashboard.py     # Dashboard interactivo con Streamlit
├── requirements.txt
└── README.md
```

## Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd customer_churn_project
```

### 2. Configurar entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Preparar los datos
1. Coloca el archivo `WA_Fn-UseC_-Telco-Customer-Churn.csv` en la carpeta `data/raw/`
2. Ejecuta el pipeline ETL:
```bash
python src/etl.py
```

### 4. Entrenar el modelo
```bash
mkdir -p models  # Crear carpeta si no existe
python src/train.py
```

## Uso del Sistema

### Ejecutar la API
Para iniciar la API de predicción:
```bash
uvicorn app.api:app --reload
```
La API estará disponible en `http://localhost:8000`

### Ejecutar el Dashboard
Para iniciar el dashboard interactivo:
```bash
streamlit run app/dashboard.py
```
El dashboard estará disponible en `http://localhost:8501`

## API de Predicción

### Endpoint de Predicción
**POST** `/predict`

### Ejemplo de solicitud
Envía una solicitud POST a `http://localhost:8000/predict` con el siguiente formato JSON:

```json
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
```

### Ejemplo de respuesta
```json
{
  "churn_probability": 0.75,
  "prediction": "Yes",
  "confidence": "High"
}
```

## Características del Dataset

El modelo utiliza las siguientes características del cliente:
- **Demográficas:** Género, edad (senior citizen), partner, dependents
- **Servicios:** Teléfono, múltiples líneas, internet, seguridad online, backup, etc.
- **Contractuales:** Tipo de contrato, facturación sin papel, método de pago
- **Financieras:** Cargos mensuales, cargos totales, tiempo de permanencia

## Modelo de Machine Learning

- **Algoritmo:** XGBoost Classifier
- **Métricas de evaluación:** Accuracy, Precision, Recall, F1-Score
- **Validación:** Cross-validation y conjunto de prueba
- **Características:** Manejo automático de valores faltantes y codificación de variables categóricas

## Funcionalidades del Dashboard

- Visualización de distribución de churn
- Análisis exploratorio de datos
- Predicciones individuales interactivas
- Métricas del modelo
- Gráficos de importancia de características

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

