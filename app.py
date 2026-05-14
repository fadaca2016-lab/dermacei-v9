import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración de la Página
st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

# 2. Encendido del Motor (Configuración de IA)
try:
    # Traemos la llave desde los Secrets de Streamlit
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Usamos 'gemini-pro-vision', que es el modelo más estable para fotos 
    # y evita el error de "modelo no encontrado" en versiones viejas.
    model = genai.GenerativeModel('gemini-pro-vision')
except Exception as e:
    st.error(f"Falla en el encendido del sistema: {e}")

# 3. Interfaz del CEI
st.title("🚀 Derma CEI v2.0 - V8 Edition")
st.sidebar.header("Menú Técnico CEI")
opcion = st.sidebar.radio("Seleccioná Función:", ["Escáner de Piel", "Análisis INCI Pro"])

# --- LÓGICA DEL ESCÁNER ---
if opcion == "Escáner de Piel":
    st.subheader("🔍 Diagnóstico Técnico de Biotipo y Lesiones")
    st.info("Subí la foto del gabinete para detectar comedones, pápulas y pústulas.")
    
    foto = st.file_uploader("Cargar imagen de la piel", type=['jpg', 'png', 'jpeg'])
    
    if foto:
        img = Image.open(foto)
        st.image(img, width=450, caption="Imagen cargada")
        
        if st.button("🚀 INICIAR ESCANEO POR IA"):
            with st.spinner("El sistema está analizando el tejido..."):
                try:
                    # Instrucciones precisas para el diagnóstico del CEI
                    prompt = (
                        "Actúa como un experto técnico del CEI (Centro de Estética Integral). "
                        "Analiza la imagen adjunta y determina: "
                        "1. Biotipo cutáneo predominante. "
                        "2. Presencia de lesiones (comedones, pápulas y pústulas). "
                        "3. Sugerencia de protocolo técnico con aparatología (ej. electroporación) "
                        "priorizando el uso de activos sobre marcas comerciales."
                    )
                    
                    # Ejecución del análisis
                    response = model.generate_content([prompt, img])
                    st.markdown("### 📊 Informe Técnico del CEI")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error("El motor no pudo procesar la imagen. Intentá refrescar la página o hacer un Reboot.")

# --- LÓGICA DE INCI ---
elif opcion == "Análisis INCI Pro":
    st.subheader("🧪 Laboratorio de Activos")
    inci_input = st.text_area("Pegá el listado INCI aquí:")
    
    if st.button("Analizar Activos"):
        if inci_input:
            with st.spinner("Estudiando fórmula..."):
                # Para texto usamos el modelo flash que es más rápido
                model_text = genai.GenerativeModel('gemini-1.5-flash')
                res = model_text.generate_content(f"Analiza este INCI: {inci_input}. Identifica activos clave y riesgos.")
                st.write(res.text)
