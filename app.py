import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración de la Llave (Desde los Secrets de Streamlit)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("Falta la configuración de la llave GEMINI_API_KEY en los Secrets.")

# Configuración de la página
st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

# 2. Título y Menú Lateral
st.title("🚀 Derma CEI v2.0 - V8 Edition")
st.sidebar.header("Menú Técnico CEI")
opcion = st.sidebar.radio("Seleccioná una función:", 
                         ["Escáner de Piel", "Análisis de Cosméticos (INCI)", "Lámpara de Wood Digital"])

# 3. Función: Escáner de Piel (Diagnóstico y Protocolo)
if opcion == "Escáner de Piel":
    st.subheader("🔍 Análisis de Biotipo y Lesiones")
    st.info("Subí una foto nítida para detectar comedones, pápulas o pústulas.")
    
    foto = st.file_uploader("Cargar imagen de la piel", type=['jpg', 'png', 'jpeg'])
    
    if foto:
        img = Image.open(foto)
        st.image(img, width=450, caption="Imagen cargada para análisis")
        
        if st.button("🚀 INICIAR ESCANEO POR IA"):
            # Usamos el modelo más estable para visión
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = (
                "Actúa como un experto técnico del CEI (Centro de Estética Integral). "
                "Analiza la imagen adjunta con rigor profesional: "
                "1. Determina el biotipo cutáneo predominante. "
                "2. Identifica y cuantifica lesiones: comedones, pápulas y pústulas. "
                "3. Sugiere un protocolo técnico basado en aparatología (ej. electroporación) "
                "priorizando activos sobre marcas comerciales."
            )
            
            with st.spinner("El sistema está analizando el tejido..."):
                try:
                    response = model.generate_content([prompt, img])
                    st.markdown("### 📊 Informe Técnico del CEI")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error en el motor: {e}. Verificá que la API Key sea correcta.")

# 4. Función: Análisis de Cosméticos (INCI)
elif opcion == "Análisis de Cosméticos (INCI)":
    st.subheader("🧪 Laboratorio de Activos (INCI)")
    st.write("Estudio de principios activos según nomenclatura internacional.")
    
    texto_inci = st.text_area("Pegá aquí el listado INCI del producto:")
    
    if st.button("Analizar Componentes"):
        if texto_inci:
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt_inci = (
                f"Analiza el siguiente INCI: {texto_inci}. "
                "Identifica los activos principales y su función. "
                "Advierte si hay riesgo de irritación o incompatibilidades químicas (ej. Niacinamida en pH bajos)."
            )
            with st.spinner("Estudiando la fórmula..."):
                response = model.generate_content(prompt_inci)
                st.markdown("### 🧬 Desglose de Activos")
                st.write(response.text)
        else:
            st.warning("Por favor, ingresá un texto para analizar.")

# 5. Función: Lámpara de Wood Digital
elif opcion == "Lámpara de Wood Digital":
    st.subheader("💡 Simulación de Fluorescencia UV")
    st.write("Ajuste de contraste técnico para visualizar porfirinas y manchas profundas.")
    
    foto_wood = st.file_uploader("Subí la foto para filtrar", type=['jpg', 'png', 'jpeg'])
    
    if foto_wood:
        # Aquí mostramos la foto; en versiones futuras podemos aplicar filtros de imagen
        st.image(foto_wood, caption="Simulación de contraste Wood activada", width=450)
        st.warning("Esta es una simulación visual. No reemplaza el uso de la lámpara física en gabinete.")

st.sidebar.markdown("---")
st.sidebar.write("CEI - Cosmetología desde Cero")
