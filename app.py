import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración de la Página
st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

# 2. Conexión con el Cerebro de la IA
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception:
    st.error("Falla en la configuración inicial. Revisá la API Key.")

st.title("🚀 Derma CEI v2.0 - V8 Edition")
st.sidebar.header("Menú Técnico CEI")
opcion = st.sidebar.radio("Función:", ["Escáner de Piel", "Análisis INCI Pro"])

# --- ESCÁNER DE PIEL ---
if opcion == "Escáner de Piel":
    st.subheader("🔍 Diagnóstico Técnico de Biotipo y Lesiones")
    foto = st.file_uploader("Subí la foto del gabinete", type=['jpg', 'png', 'jpeg'])
    
    if foto:
        img = Image.open(foto)
        
        # MECÁNICA DE GUERRILLA: Achicamos la foto para que pase por el caño sin trabarse
        # Redimensionamos a un máximo de 800px manteniendo la proporción
        ancho, alto = img.size
        proporcion = 800 / float(ancho)
        nuevo_alto = int((float(alto) * proporcion))
        img_reducida = img.resize((800, nuevo_alto), Image.LANCZOS)
        
        st.image(img_reducida, width=400, caption="Imagen procesada para el CEI")
        
        if st.button("🚀 INICIAR ESCANEO POR IA"):
            with st.spinner("Analizando tejido en profundidad..."):
                try:
                    # Prompt optimizado para resultados de gabinete
                    prompt = (
                        "Actúa como experto técnico del CEI. Analiza esta piel: "
                        "1. Determina biotipo cutáneo. "
                        "2. Detecta lesiones: comedones, pápulas y pústulas. "
                        "3. Sugiere protocolo con aparatología (ej. electroporación) sin marcas."
                    )
                    
                    response = model.generate_content([prompt, img_reducida])
                    st.success("¡Análisis completado!")
                    st.markdown("### 📊 Resultado Técnico")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error(f"El motor está saturado. Probá con una captura de pantalla: {e}")

# --- ANÁLISIS INCI ---
elif opcion == "Análisis INCI Pro":
    st.subheader("🧪 Laboratorio de Activos")
    inci = st.text_area("Pegá el listado INCI aquí:")
    if st.button("Analizar Fórmula"):
        if inci:
            with st.spinner("Estudiando activos..."):
                res = model.generate_content(f"Analiza este INCI: {inci}. Identifica activos clave.")
                st.write(res.text)
