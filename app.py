import streamlit as st
from PIL import Image
import os

# Configuración de la página
st.set_page_config(
    page_title="Mi primera aplicación de Streamlit",
    page_icon="📊",
    layout="wide"
)

# 1. Preparación y Carga de Logo (Opcional si no se tiene imagen física, se maneja de forma segura)
logo_path = ""
has_logo = os.path.exists(logo_path)

# 3. Barra lateral (st.sidebar)
with st.sidebar:
    st.header("Mi primera barra lateral de Streamlit")
    st.write("¡Hola! Este es el panel lateral de control y navegación de la aplicación.")
    
    if has_logo:
        st.image(logo_path, width=150)
    else:
        st.info("💡 [Logo institucional aquí]")
        
    st.markdown("---")
    
    # Botón lateral y campo de texto lateral
    boton_lateral = st.button("Acción Lateral")
    
    texto_barra = st.text_input("Escribe algo en la barra", key="sidebar_text")
    
    if boton_lateral:
        st.success("¡Botón lateral presionado con éxito!")
        
    st.markdown("---")
    st.subheader("Resultado en la barra:")
    if texto_barra.strip() != "":
        st.write(f"Escribiste: {texto_barra}")
    else:
        st.warning("Por favor, escribe un mensaje en la barra.")

# 2. Área principal
st.title("Mi primera aplicación de Streamlit")
st.header("¡Bienvenido a tu panel interactivo!")
st.write("Esta aplicación demuestra el uso de entradas de datos, botones y la organización de controles entre el área principal y la barra lateral.")

# Mostrar logo en área principal si existe
if has_logo:
    st.image(logo_path, width=200)

st.markdown("---")

# Botón principal y campo de texto principal
col1, col2 = st.columns([1, 2])

with col1:
    boton_principal = st.button("Haz clic")
    if boton_principal:
        st.balloons()
        st.success("¡El botón principal fue presionado!")

with col2:
    texto_principal = st.text_input("Escribe algo", key="main_text")
    
    st.markdown("### Salida principal:")
    if texto_principal.strip() != "":
        st.write(f"Escribiste: {texto_principal}")
    else:
        st.info("Escribe un mensaje para ver el resultado reflejado aquí.")
