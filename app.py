import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración de la Página
st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

# 2. Conexión de Seguridad (La que no falla)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Usamos el nombre del modelo sin el prefijo 'models/' que es lo que suele tirar el 404
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Falla de configuración: {e}")

st.title("🚀 Derma CEI v2.0 - V8 Edition")

# 3. Interfaz del CEI
foto = st.file_uploader("Subí la foto del gabinete", type=['jpg', 'png', 'jpeg'])

if foto:
    img = Image.open(foto)
    # Optimizamos la imagen para que no pese (Mecánica de guerrilla)
    img.thumbnail((800, 800))
    st.image(img, width=400, caption="Imagen lista para el CEI")
    
    if st.button("🚀 INICIAR ESCANEO POR IA"):
        with st.spinner("Analizando tejido en profundidad..."):
            try:
                # El prompt técnico que le enseñamos a las alumnas
                prompt = (
                    "Actúa como experto técnico del CEI. Analiza esta piel: "
                    "1. Determina biotipo cutáneo. "
                    "2. Identifica comedones, pápulas y pústulas. "
                    "3. Sugiere protocolo con aparatología (ej. electroporación) sin marcas."
                )
                
                # Llamada directa al motor
                response = model.generate_content([prompt, img])
                
                st.success("¡Análisis completado!")
                st.markdown("### 📊 Informe Técnico")
                st.write(response.text)
                
            except Exception as e:
                # Si falla, te mostramos el error real para cazarlo de una
                st.error(f"Error en el motor de IA: {e}")
                st.info("Tip: Si dice '404', probá haciendo un 'Reboot' desde el menú Manage App.")
