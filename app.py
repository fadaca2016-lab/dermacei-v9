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
opcion = st.sidebar.radio("Función:", ["Escáner de Piel", "Análisis INCI", "Simulador Wood"])

# 3. Lógica del Escáner (Pata 1 y 4)
if opcion == "Escáner de Piel":
    st.subheader("🔍 Diagnóstico Técnico de Piel")
    foto = st.file_uploader("Subí la foto del gabinete", type=['jpg', 'png', 'jpeg'])
    
    if foto:
        img = Image.open(foto)
        st.image(img, width=400)
        
        # EL BOTÓN: Ahora afuera y visible
        if st.button("🚀 INICIAR ESCANEO POR IA"):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = "Actúa como experto del CEI. Analiza esta piel. Detecta biotipo, comedones, pápulas y pústulas. Luego sugiere un protocolo técnico (ej. electroporación) sin mencionar marcas."
            
            with st.spinner("Analizando tejido..."):
                response = model.generate_content([prompt, img])
                st.markdown("### 📊 Resultado del Análisis")
                st.write(response.text)

# 4. Lógica de Cosméticos (Pata 2)
elif opcion == "Análisis INCI":
    st.subheader("🧪 Laboratorio de Activos")
    inci = st.text_area("Pegá el INCI aquí:")
    if st.button("Estudiar Fórmula"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Analiza este INCI: {inci}. Identifica activos y advierte sobre Niacinamida en pH bajos.")
        st.write(response.text)

# 5. Simulador Wood (Pata 3)
elif opcion == "Simulador Wood":
    st.subheader("💡 Lámpara de Wood Digital")
    foto_w = st.file_uploader("Subí foto para filtro", type=['jpg', 'png', 'jpeg'])
    if foto_w:
        st.image(foto_w, caption="Simulación UV activada", width=400)
