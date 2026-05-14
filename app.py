# --- PATA 1 & 4: DIAGNÓSTICO Y PROTOCOLO ---
if opcion == "Escáner de Piel y Lesiones":
    st.subheader("🔍 Diagnóstico Técnico de Piel")
    foto = st.file_uploader("Subí la foto del gabinete", type=['jpg', 'png', 'jpeg'])
    
    if foto:
        img = Image.open(foto)
        st.image(img, width=400)
        
        # El botón ahora está afuera para que no se esconda
        if st.button("Iniciar Escaneo por IA"):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = "Actúa como experto del CEI. Analiza esta piel. Detecta biotipo, comedones, pápulas y pústulas. Luego sugiere un protocolo técnico (ej. electroporación) sin mencionar marcas ni nombres propios."
            
            with st.spinner("Analizando tejido..."):
                try:
                    response = model.generate_content([prompt, img])
                    st.markdown("### 📊 Resultado del Análisis")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Hubo un problema con la llave: {e}")
