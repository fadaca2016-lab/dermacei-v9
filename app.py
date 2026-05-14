import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración de la Llave
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Error: Revisá que la API Key esté bien pegada en 'Secrets'.")

st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

# 2. Interfaz
st.title("🚀 Derma CEI v2.0 - V8 Edition")
st.sidebar.header("Menú Técnico CEI")
opcion = st.sidebar.radio("Función:", ["Escáner de Piel", "Análisis INCI", "Simulador Wood"])

# 3. Lógica del Escáner
if opcion == "Escáner de Piel":
    st.subheader("🔍 Diagnóstico Técnico")
    foto = st.file_uploader("Subí la foto", type=['jpg', 'png', 'jpeg'])
    
    if foto:
        img = Image.open(foto)
        st.image(img, width=400)
        
        if st.button("🚀 INICIAR ESCANEO POR IA"):
            with st.spinner("Analizando tejido..."):
                # Probamos con el nombre del modelo más estable
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = "Analiza biotipo y lesiones (comedones, pápulas, pústulas). Sugiere protocolo técnico sin marcas."
                    response = model.generate_content([prompt, img])
                    st.success("¡Análisis Completado!")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"El motor principal está regulando mal. Intentando con motor de reserva...")
                    # Motor de reserva por si la librería es vieja
                    try:
                        model_alt = genai.GenerativeModel('gemini-pro-vision')
                        response = model_alt.generate_content([prompt, img])
                        st.write(response.text)
                    except:
                        st.error("Error crítico: Por favor, reiniciá la app desde 'Manage App' -> 'Reboot'.")

# 4. Otras Funciones
elif opcion == "Análisis INCI":
    st.subheader("🧪 Laboratorio de Activos")
    inci = st.text_area("INCI:")
    if st.button("Analizar"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        res = model.generate_content(f"Analiza activos de este INCI: {inci}")
        st.write(res.text)
