import streamlit as st
import os
import pandas as pd
from pypdf import PdfReader
from dotenv import load_dotenv
from google import genai
from google.genai import types

# 1. Cargar la API Key
load_dotenv()
api_key = os.getenv("pasion-futbolera-bot")

st.set_page_config(page_title="Pasión Futbolera Bot", page_icon="⚽")
st.title("⚽ Asistente Virtual - Pasión Futbolera")

# 2. Función para leer documentos PDF y CSV de la carpeta 'data'
@st.cache_data
def cargar_documentos():
    texto_contexto = ""
    data_dir = "data"
    
    if os.path.exists(data_dir):
        for archivo in os.listdir(data_dir):
            ruta_archivo = os.path.join(data_dir, archivo)
            
            # Leer archivos PDF
            if archivo.endswith(".pdf"):
                try:
                    reader = PdfReader(ruta_archivo)
                    texto_contexto += f"\n--- DOCUMENTO: {archivo} ---\n"
                    for page in reader.pages:
                        texto_contexto += page.extract_text() + "\n"
                except Exception as e:
                    st.warning(f"No se pudo leer {archivo}: {e}")
                    
            # Leer archivos CSV
            elif archivo.endswith(".csv"):
                try:
                    df = pd.read_csv(ruta_archivo)
                    texto_contexto += f"\n--- INVENTARIO / TABLA: {archivo} ---\n"
                    texto_contexto += df.to_string() + "\n"
                except Exception as e:
                    st.warning(f"No se pudo leer {archivo}: {e}")
                    
    return texto_contexto

contexto_tienda = cargar_documentos()

# 3. Instrucción del sistema para la IA
instrucciones_sistema = f"""
Eres el asistente inteligente oficial de la tienda online "Pasión Futbolera".
Tu objetivo es responder las consultas de los clientes con un tono amable, profesional y entusiasta sobre el fútbol.

Usa ÚNICAMENTE la siguiente información oficial para responder preguntas sobre precios, tallas, inventario, políticas de envío, reembolsos y términos:
==================================================
{contexto_tienda}
==================================================

Reglas:
- Si el usuario pregunta qué camisetas o tallas hay disponibles, consulta la sección de inventario y responde con precisión.
- Si te preguntan algo que no está en la información proporcionada, responde amablemente indicando que no posees esa información y sugiere contactar al equipo de soporte.
"""

# 4. Lógica del Chat
if not api_key:
    st.error("⚠️ Falta la clave pasion-futbolera-bot en el archivo .env")
else:
    client = genai.Client(api_key=api_key)

    # Mantener el historial de la conversación
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "¡Hola! Bienvenido a **Pasión Futbolera** ⚽. ¿En qué puedo ayudarte hoy?"}
        ]

    # Mostrar mensajes anteriores
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Entrada del usuario
    if prompt := st.chat_input("Escribe tu pregunta aquí..."):
        # Registrar y mostrar mensaje del usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generar respuesta
        with st.chat_message("assistant"):
            with st.spinner("Consultando información de la tienda..."):
                try:
                    response = client.models.generate_content(
                        model='gemini-3.5-flash',
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            system_instruction=instrucciones_sistema,
                            temperature=0.3
                        )
                    )
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"Error al conectar con la IA: {e}")