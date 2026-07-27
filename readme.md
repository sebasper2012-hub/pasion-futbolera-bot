# ⚽ Pasión Futbolera - Agente Inteligente de Atención al Cliente

Proyecto desarrollado como solución al **Challenge Agente Inteligente** de **ALURA Latam**.

---

## 📌 1. Descripción General del Proyecto
**Pasión Futbolera Bot** es un agente conversacional inteligente diseñado para actuar como el asistente virtual oficial de una tienda de comercio electrónico de camisetas de fútbol. 

El agente resuelve un problema real de atención al cliente al responder automáticamente consultas sobre:
* **Inventario:** Disponibilidad de camisetas de equipos (Real Madrid, Barcelona, Manchester United, Olimpia, Palmeiras), precios en USD y tallas (P, M, G, XG).
* **Políticas de la tienda:** Tiempos y costos de envío, métodos de rastreo, devoluciones, reembolsos y términos de privacidad.

Toda la información proporcionada por la IA se basa estrictamente en documentos oficiales (PDFs y CSVs) de la tienda.

---

## 🏗️ 2. Arquitectura de la Solución

text
 [ Usuario ] 
     │
     ▼ (Interacción mediante chat web)
 [ Interfaz Streamlit (Streamlit Cloud) ]
     │
     ├── 1. Carga de Documentos Locales (data/)
     │      ├── inventario.csv ──► Pandas (DataFrame)
     │      └── politicas.pdf  ──► PyPDF (Extracción de Texto)
     │
     ├── 2. Construcción de Contexto e Instrucción del Sistema
     │
     ▼ (Prompt + Contexto de Documentos)
 [ Google Gemini API (gemini-3.5-flash) ]
     │
     ▼ (Respuesta Precisa)
 [ Interfaz Streamlit ] ──► [ Usuario ]
 
🛠️ 3. Tecnologías y Herramientas Utilizadas
Lenguaje de Programación: Python 3.12+

Modelo de Lenguaje (LLM): Google Gemini API (gemini-3.5-flash)

Interfaz Web: Streamlit

Procesamiento de Datos: Pandas (para inventario CSV) y PyPDF (para políticas PDF)

Gestión de Entorno: python-dotenv y Entorno Virtual (venv)

Control de Versiones: Git & GitHub

Despliegue en la Nube: Streamlit Community Cloud

🚀 4. Instrucciones para Ejecutar el Proyecto Localmente
Prerrequisitos
Tener instalado Python 3.10 o superior.

Tener una clave de API de Google Gemini (Google AI Studio).

Pasos de Instalación
Clonar el repositorio:

Bash
git clone [https://github.com/sebasper2012-hub/pasion-futbolera-bot.git](https://github.com/sebasper2012-hub/pasion-futbolera-bot.git)
cd pasion-futbolera-bot
Crear y activar el entorno virtual:

En Windows (PowerShell):

PowerShell
py -m venv venv
.\venv\Scripts\activate
Instalar las dependencias:

Bash
py -m pip install -r requirements.txt
Configurar las variables de entorno:
Crea un archivo llamado .env en la raíz del proyecto y añade tu API Key:

Fragmento de código
GEMINI_API_KEY="tu_clave_de_gemini_aqui"
Ejecutar la aplicación:

Bash
streamlit run app.py
❓ 5. Ejemplos de Preguntas que el Agente Puede Responder
"¿Tienen disponible la camiseta del Club Olimpia y cuánto cuesta?"

"¿Cuáles son las tallas disponibles para la camiseta del Real Madrid?"

"¿Cuál es la política de devoluciones y cuántos días tengo para solicitarla?"

"¿Hacen envíos internacionales y cuánto tardan?"

"¿Venden camisetas originales o réplicas?"

💬 6. Ejemplos de Respuestas Generadas por el Agente
Ejemplo 1: Consulta de Inventario y Precio
Usuario: "¿Tienen la camiseta del Manchester United en talla M y cuál es el precio?" > Bot: "¡Hola! ⚽ Sí, tenemos en stock la camiseta titular del Manchester United. Está disponible en talla M (así como en P, G y XG) a un precio de $85.00 USD. ¿Te gustaría saber cómo realizar tu compra?"

Ejemplo 2: Consulta de Políticas de Envío
Usuario: "¿Cuánto tarda en llegar un envío nacional?" > Bot: "Los envíos nacionales estándar toman entre 3 a 5 días hábiles. Si necesitas tu pedido más rápido, contamos con envío exprés que tarda de 1 a 2 días hábiles. Ten en cuenta que el envío es gratuito en compras superiores a $50 USD."

☁️ 7. Evidencia del Despliegue
La aplicación se encuentra desplegada y lista para usar de manera pública en la nube: https://pasion-futbolera-bot-vzrqnvx5hzrjfzgxprq3da.streamlit.app/