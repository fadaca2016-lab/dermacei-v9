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
            # Probamos con el nombre más genérico posible para evitar el error 404
            with st.spinner("Analizando tejido..."):
                try:
                    # Usamos 'gemini-pro-vision' que es el estándar de oro para fotos
                    model = genai.GenerativeModel('gemini-pro-vision')
                    
                    prompt = (
                        "Analiza esta imagen como un experto del CEI. "
                        "Identifica biotipo cutáneo y lesiones como comedones, pápulas o pústulas. "
                        "Sugiere un protocolo técnico con aparatología sin mencionar marcas."
                    )
                    
                    response = model.generate_content([prompt, img])
                    st.markdown("### 📊 Resultado del Análisis Técnico")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"El motor gemini-pro-vision no respondió. Intentando con motor alternativo...")
                    try:
                        # Si falla, intentamos con el motor flash pero con el nombre corto
                        model_alt = genai.GenerativeModel('gemini-1.5-flash-latest')
                        response = model_alt.generate_content([prompt, img])
                        st.write(response.text)
                    except Exception as e2:
                        st.error(f"Error técnico persistente: {e2}")

# 4. Lógica de Cosméticos
elif opcion == "Análisis INCI Pro":
    st.subheader("🧪 Laboratorio de Activos")
    inci = st.text_area("Pegá el INCI aquí:")
    if st.button("Analizar Fórmula"):
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(f"Analiza este INCI: {inci}. Identifica activos clave.")
        st.write(response.text)

# 5. Simulador Wood
elif opcion == "Simulador Wood":
    st.subheader("💡 Lámpara de Wood Digital")
    foto_w = st.file_uploader("Subí foto", type=['jpg', 'png', 'jpeg'])
    if foto_w:
        st.image(foto_w, caption="Filtro UV", width=400)
