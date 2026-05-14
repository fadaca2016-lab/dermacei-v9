import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración de la Llave
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Falta la llave GEMINI_API_KEY en los Secrets.")

st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

# 2. Título y Menú
st.title("🚀 Derma CEI v2.0 - V8 Edition")
st.sidebar.header("Menú Técnico CEI")
opcion = st.sidebar.radio("Función:", ["Escáner de Piel", "Análisis INCI Pro", "Simulador Wood"])

# 3. Lógica del Escáner
if opcion == "Escáner de Piel":
    st.subheader("🔍 Diagnóstico Técnico de Piel")
    foto = st.file_uploader("Subí la foto del gabinete", type=['jpg', 'png', 'jpeg'])
    
    if foto:
        img = Image.open(foto)
        st.image(img, width=400)
        
        if st.button("🚀 INICIAR ESCANEO POR IA"):
            # Usamos el nombre simplificado que es el que acepta la versión actual
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = (
                "Analiza la imagen adjunta como un experto en dermatología cosmética. "
                "1. Identifica biotipo cutáneo. "
                "2. Detecta lesiones: comedones, pápulas y pústulas. "
                "3. Sugiere un protocolo técnico basado en aparatología (ej. electroporación) "
                "sin mencionar marcas."
            )
            
            with st.spinner("Escaneando tejido..."):
                try:
                    # Forzamos el uso del modelo con una configuración más robusta
                    response = model.generate_content([prompt, img])
                    st.markdown("### 📊 Resultado del Análisis Técnico")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error técnico en el motor: {e}")

# 4. Lógica de Cosméticos
elif opcion == "Análisis INCI Pro":
    st.subheader("🧪 Laboratorio de Activos")
    inci = st.text_area("Pegá el INCI aquí:")
    if st.button("Analizar Fórmula"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Analiza este INCI: {inci}. Identifica activos clave y riesgos químicos.")
        st.write(response.text)

# 5. Simulador Wood
elif opcion == "Simulador Wood":
    st.subheader("💡 Lámpara de Wood Digital")
    foto_w = st.file_uploader("Subí foto", type=['jpg', 'png', 'jpeg'])
    if foto_w:
        st.image(foto_w, caption="Simulación UV", width=400)
