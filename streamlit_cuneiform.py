import streamlit as st

# Diccionario: letras españolas a signos cuneiformes aproximados
cuneiforme_dict = {
    "A": "𒀀", "B": "𒁀", "C": "𒆠", "D": "𒁕", "E": "𒂊",
    "F": "𒉺", "G": "𒄀", "H": "𒄩", "I": "𒄿", "J": "𒅆",
    "K": "𒆠", "L": "𒇻", "M": "𒈠", "N": "𒉌", "Ñ": "𒉏",
    "O": "𒍝", "P": "𒉺", "Q": "𒆩", "R": "𒊑", "S": "𒊓",
    "T": "𒋼", "U": "𒌋", "V": "𒉺", "W": "𒉺𒇻", "X": "𒅆𒋼",
    "Y": "𒌒", "Z": "𒍝𒊓"
}

# Función para traducir
def traducir_a_cuneiforme(texto):
    texto = texto.upper()
    traduccion = ""
    for letra in texto:
        if letra in cuneiforme_dict:
            traduccion += cuneiforme_dict[letra] + " "
        else:
            traduccion += letra
    return traduccion

# Título y descripción
st.title("Traductor Español → Cuneiforme (aproximación)")
st.write("Escribe tu texto en español y se convertirá en signos cuneiformes.")

# Entrada de texto
texto_usuario = st.text_input("Ingresa tu texto aquí:")

# Botón para traducir
if st.button("Traducir"):
    resultado = traducir_a_cuneiforme(texto_usuario)
    st.subheader("Texto en cuneiforme:")
    st.write(resultado)
