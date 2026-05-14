import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuración de página
st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

# Conexión Segura
def iniciar_motor():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('gemini-1.5-flash')
    except:
        return None

model = iniciar_motor()

st.title("🚀 Derma CEI v2.0 - V8 Edition")

if model is None:
    st.error("Error de conexión. Revisá la API Key en los Secrets.")
else:
    foto = st.file_uploader("Subí la foto del gabinete", type=['jpg', 'png', 'jpeg'])
    
    if foto:
        img = Image.open(foto)
        st.image(img, width=400)
        
        if st.button("🚀 INICIAR ESCANEO POR IA"):
            with st.spinner("Analizando tejido..."):
                try:
                    # Instrucciones técnicas del CEI
                    prompt = "Analiza biotipo y lesiones (comedones, pápulas, pústulas). Sugiere protocolo técnico sin marcas."
                    response = model.generate_content([prompt, img])
                    st.success("Análisis técnico completado")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Falla técnica: {e}")
