import streamlit as st
import google.generativeai as genai
from PIL import Image
import time

# Configuración técnica del CEI
st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Probamos con el modelo flash-latest que es el más veloz para evitar cortes
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except:
    st.error("Revisá la configuración de la API Key.")

st.title("🚀 Derma CEI v2.0 - V8 Edition")
st.sidebar.header("Menú Técnico CEI")
opcion = st.sidebar.radio("Función:", ["Escáner de Piel", "Análisis INCI Pro"])

if opcion == "Escáner de Piel":
    st.subheader("🔍 Diagnóstico de Biotipo y Lesiones")
    foto = st.file_uploader("Subí la foto del gabinete", type=['jpg', 'png', 'jpeg'])
    
    if foto:
        img = Image.open(foto)
        st.image(img, width=400)
        
        if st.button("🚀 INICIAR ESCANEO POR IA"):
            with st.spinner("Analizando tejido..."):
                # Damos un respiro al servidor
                time.sleep(1) 
                try:
                    prompt = (
                        "Analiza esta piel como experto del CEI. "
                        "Identifica biotipo y lesiones: comedones, pápulas y pústulas. "
                        "Sugerí protocolo con aparatología sin mencionar marcas comerciales."
                    )
                    # Forzamos el envío limpio de la imagen
                    response = model.generate_content([prompt, img])
                    st.success("¡Análisis completado!")
                    st.markdown("### 📊 Resultado Técnico")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"El motor está ocupado o la imagen es muy pesada. Intentá de nuevo en 5 segundos.")
