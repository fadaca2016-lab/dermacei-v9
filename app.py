import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuración técnica
st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

# Conexión al cerebro de la IA
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Nombre de modelo universalmente compatible
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Error de configuración inicial.")

st.title("🚀 Derma CEI v2.0 - V8 Edition")

foto = st.file_uploader("Subí la foto del gabinete", type=['jpg', 'png', 'jpeg'])

if foto:
    img = Image.open(foto)
    st.image(img, width=400)
    
    if st.button("🚀 INICIAR ESCANEO POR IA"):
        with st.spinner("Analizando tejido..."):
            try:
                # Instrucciones del CEI para detectar lesiones
                prompt = (
                    "Actúa como experto del CEI. Analiza esta piel con precisión técnica. "
                    "Detecta biotipo cutáneo y lesiones: comedones, pápulas y pústulas. "
                    "Sugiere protocolo con aparatología (ej. electroporación) sin mencionar marcas."
                )
                
                # Ejecución del motor
                response = model.generate_content([prompt, img])
                st.success("Análisis completado")
                st.markdown("### 📊 Resultado Técnico")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Falla técnica en el motor: {e}")
