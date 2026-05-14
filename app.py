import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración del CEI
st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

# 2. Encendido forzado del motor
@st.cache_resource
def configurar_ia():
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        # Probamos el nombre directo sin prefijos
        return genai.GenerativeModel('gemini-1.5-flash')
    except:
        return None

model = configurar_ia()

st.title("🚀 Derma CEI v2.0 - V8 Edition")

# 3. Interfaz de Gabinete
foto = st.file_uploader("Subí la foto", type=['jpg', 'png', 'jpeg'])

if foto:
    img = Image.open(foto)
    # Reducción técnica de peso
    img.thumbnail((800, 800))
    st.image(img, width=400, caption="Imagen lista para el CEI")
    
    if st.button("🚀 INICIAR ESCANEO POR IA"):
        if model is None:
            st.error("Falla crítica de configuración. Revisá los Secrets.")
        else:
            with st.spinner("Analizando tejido..."):
                try:
                    prompt = (
                        "Analiza esta piel como experto del CEI. "
                        "Detecta biotipo y lesiones: comedones, pápulas y pústulas. "
                        "Sugiere protocolo con aparatología sin marcas."
                    )
                    response = model.generate_content([prompt, img])
                    st.success("¡Análisis completado!")
                    st.markdown("### 📊 Informe Técnico")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error en el motor: {e}")
                    st.info("Hacé un 'Reboot' desde el menú Manage App para limpiar la memoria.")
