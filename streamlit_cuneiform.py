import streamlit as st

# Diccionario: letras españolas a signos cuneiformes aproximados
spanish_to_sumerian = {
    "A": "𒀀", "B": "𒁀", "C": "𒆠", "D": "𒁕", "E": "𒂊",
    "F": "𒉺", "G": "𒄀", "H": "𒄩", "I": "𒄿", "J": "𒅆",
    "K": "𒆠", "L": "𒇻", "M": "𒈠", "N": "𒉌", "Ñ": "𒉏",
    "O": "𒍝", "P": "𒉺", "Q": "𒆩", "R": "𒊑", "S": "𒊓",
    "T": "𒋼", "U": "𒌋", "V": "𒉺", "W": "𒉺𒇻", "X": "𒅆𒋼",
    "Y": "𒌒", "Z": "𒍝𒊓"
}

# Crear diccionario inverso para traducir de Sumerian → Spanish
sumerian_to_spanish = {v: k for k, v in spanish_to_sumerian.items()}

# Función para traducir español → sumerio
def traducir_a_sumerio(texto):
    texto = texto.upper()
    traduccion = ""
    for letra in texto:
        if letra in spanish_to_sumerian:
            traduccion += spanish_to_sumerian[letra] + " "
        else:
            traduccion += letra
    return traduccion

# Función para traducir sumerio → español
def traducir_a_espanol(texto):
    # Separar los signos por espacio (porque así se generan en español → sumerio)
    signos = texto.split(" ")
    traduccion = ""
    for signo in signos:
        if signo in sumerian_to_spanish:
            traduccion += sumerian_to_spanish[signo]
        else:
            traduccion += signo
    return traduccion

# Título de la app
st.title("Traductor Español ↔ Sumerio (aproximación)")

# Selección de dirección de traducción
direccion = st.radio("Selecciona la dirección de traducción:", 
                     ("Español → Sumerio", "Sumerio → Español"))

# Entrada de texto
entrada = st.text_area("Ingresa tu texto:")

# Botón para traducir
if st.button("Traducir"):
    if direccion == "Español → Sumerio":
        resultado = traducir_a_sumerio(entrada)
    else:
        resultado = traducir_a_espanol(entrada)
    st.subheader("Resultado:")
    st.write(resultado)
