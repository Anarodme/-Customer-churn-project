import streamlit as st
import requests

st.title("Predicción de Fuga de Clientes")

json_input = st.text_area("Introduce datos del cliente en JSON (clave: valor)", height=300)

if st.button("Predecir"):
    try:
        data = eval(json_input)
        response = requests.post("http://localhost:8000/predict", json=data)
        st.write(response.json())
    except Exception as e:
        st.error(f"Error: {e}")
