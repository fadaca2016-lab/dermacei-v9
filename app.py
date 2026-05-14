import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuración básica
st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

# Intento de conexión directa
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Error de configuración inicial.")

st.title("🚀 Derma CEI v2.0 - V8 Edition")
opcion = st.sidebar.radio("Función:", ["Escáner de Piel", "Análisis INCI"])

if opcion == "Escáner de Piel":
    foto = st.file_uploader("Subí la foto", type=['jpg', 'png', 'jpeg'])
    if foto:
        img = Image.open(foto)
        st.image(img, width=400)
        if st.button("🚀 INICIAR ESCANEO POR IA"):
            with st.spinner("Escaneando tejido..."):
                try:
                    # El prompt técnico del CEI
                    prompt = "Analiza biotipo y lesiones (comedones, pápulas, pústulas). Sugiere protocolo técnico sin marcas."
                    response = model.generate_content([prompt, img])
                    st.success("Análisis técnico completado")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Falla en la conexión con el motor de IA: {e}")
