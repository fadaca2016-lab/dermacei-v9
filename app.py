import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración de la Página
st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

# 2. Conexión Blindada con los Motores de Google
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("Error crítico: Falta la API Key en los Secrets de Streamlit.")

st.title("🚀 Derma CEI v2.0 - V8 Edition")
st.sidebar.header("Menú Técnico CEI")
opcion = st.sidebar.radio("Función:", ["Escáner de Piel", "Análisis INCI Pro"])

# --- LÓGICA DEL ESCÁNER DE PIEL ---
if opcion == "Escáner de Piel":
    st.subheader("🔍 Diagnóstico Técnico de Biotipo y Lesiones")
    foto = st.file_uploader("Subí la foto del gabinete", type=['jpg', 'png', 'jpeg'])
    
    if foto:
        img = Image.open(foto)
        # Reducción de peso para que pase por el "caño" de internet sin trabarse
        img.thumbnail((800, 800))
        st.image(img, width=400, caption="Imagen optimizada para el CEI")
        
        if st.button("🚀 INICIAR ESCANEO POR IA"):
            with st.spinner("Analizando tejido en profundidad..."):
                prompt = (
                    "Actúa como experto técnico del CEI. Analiza esta piel: "
                    "1. Determina biotipo cutáneo. "
                    "2. Detecta lesiones: comedones, pápulas y pústulas. "
                    "3. Sugiere protocolo con aparatología (ej. electroporación) sin mencionar marcas."
                )
                
                try:
                    # Intento 1: El motor más moderno
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content([prompt, img])
                    st.success("¡Análisis completado!")
                    st.markdown("### 📊 Resultado Técnico")
                    st.write(response.text)
                except Exception:
                    try:
                        # Intento 2: El motor de reserva (para evitar el error 404)
                        model_alt = genai.GenerativeModel('gemini-pro-vision')
                        response = model_alt.generate_content([prompt, img])
                        st.success("¡Análisis completado (Motor de Reserva)!")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error técnico persistente: {e}. Por favor, hacé un Reboot desde Manage App.")

# --- LÓGICA DE ANÁLISIS INCI ---
elif opcion == "Análisis INCI Pro":
    st.subheader("🧪 Laboratorio de Activos")
    inci = st.text_area("Pegá el listado INCI aquí:")
    if st.button("Analizar Fórmula"):
        if inci:
            with st.spinner("Estudiando activos..."):
                try:
                    model_text = genai.GenerativeModel('gemini-1.5-flash')
                    res = model_text.generate_content(f"Analiza este INCI: {inci}. Identifica activos clave.")
                    st.write(res.text)
                except:
                    st.error("El motor de texto no respondió. Intentá de nuevo.")
