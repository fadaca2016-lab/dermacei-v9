import streamlit as st

st.set_page_config(page_title="Derma CEI v2.0", layout="wide")

st.title("🚀 Derma CEI v2.0 - V8 Edition")
st.write("Bienvenido, Fabio. El sistema está regulando.")

st.sidebar.header("Menú Técnico")
opcion = st.sidebar.radio("Seleccioná una función:", 
                         ["Diagnóstico de Piel", "Análisis de Cosméticos (INCI)", "Lámpara de Wood Digital"])

if opcion == "Diagnóstico de Piel":
    st.subheader("🔍 Análisis de Biotipo y Lesiones")
    st.info("Subí una foto para detectar comedones, pápulas o pústulas.")
    st.file_uploader("Cargar imagen de la piel", type=["jpg", "png", "jpeg"])

elif opcion == "Análisis de Cosméticos (INCI)":
    st.subheader("🧪 Laboratorio de Activos")
    st.write("Prioridad técnica: El activo sobre la marca.")
    st.text_input("Ingresá el INCI o componentes:")
    st.warning("Alerta de conflicto: Niacinamida + pH bajo detectado (Simulación)")

elif opcion == "Lámpara de Wood Digital":
    st.subheader("💡 Simulación de Fluorescencia")
    st.file_uploader("Subí foto para filtro de Wood", type=["jpg", "png", "jpeg"])

st.divider()
st.caption("CEI - Centro de Estética Integral | Cosmetología desde Cero")
