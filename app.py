import streamlit as st
import random
import base64

# ------------------------ CONFIGURACIÓN DE PÁGINA ------------------------
st.set_page_config(page_title="Oráculo Tóxico", layout="centered")

# ------------------------ PREDICCIONES ------------------------
predicciones = [
    "Hoy como de costumbre la vas a cagar.",
    "Descubrirás que sirves para algo, para dar cringe.",
    "Otro día solitario, aburrido y espantoso.",
    "Seguirás echándole ganas...y fallando cada vez más.",
    "Al mirarte hoy al espejo, te verás más acabado y rancio.",
    "Pensarás en lo que haz hecho con tu vida, un desperdicio de años.",
    "Hoy como todos los días serás invisible e innecesario.",
    "Tendrás otra genial idea que jamás vas a implementar.",
    "Hoy alguien te dirá -Te amo- y justo cuando le respondas despertarás.",
    "Lo estás haciendo horrible, ríndete.",
    "Todo el resto del año vas a seguir siendo inútil.",
    "Descubrirás que tienes talento para cosas absolutamente innecesarias.",
    "El cajero automático te mostrará más ceros... a la izquierda.",
    "Tendrás un día normal, es decir muy jodido.",
    "Vas a ser noticia en tu jale, tus días en la empresa están contados.",
    "Seguirás de esclavo en tu jale culero, no sirves para emprender.",
    "Hoy empezarás una nueva vida, con menos porvenir que la anterior.",
    "Estás a punto de lograrlo, superar tu récord de días seguidos sin lograr nada.",
    "¡¡ESTÁS DE SUERTE!! pide un deseo y te lo concederé.",
    "Lo estás haciendo genial, eres el ejemplo perfecto del fracaso.",
    "Tus sospechas serán ciertas, eres un farsante y te van a descubrir.",
    "Eso que creías que hacías muy bien en realidad era pura suerte.",
    "Quédate tranquilo, el Universo no te odia, todo lo malo te pasa por imbécil.",
    "Estás demasiado joven para quejarte y demasiado viejo para soñar.",
    "Solo le caes bien a pura gente mierda, y hasta ellos te ignoran.",
    "Tu crush sabe que la stalkeas, y siente asco.",
    "Tu máximo logro de hoy será no convertirte en indigente todavía.",
    "Ponte a jalar en lugar de estar jugando esta madre, por eso no progresas.",
    "Vas a comprar eso que tanto querías y después te vas a arrepentir.",
    "Hoy será un día grandioso para todos... excepto para ti."
]

# ------------------------ FUNCIONES DE APOYO ------------------------

# Fondo como imagen base64
def fondo_con_base64(ruta_imagen):
    with open(ruta_imagen, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    css = f"""
    <style>
    [data-testid="stApp"] {{
        background-image: url("data:image/jpg;base64,{data}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Música de fondo (loop)
def reproducir_audio_fondo_autoplay(ruta):
    try:
        with open(ruta, "rb") as audio_file:
            audio_bytes = audio_file.read()
            audio_base64 = base64.b64encode(audio_bytes).decode()
            audio_html = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3" />
            </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ No se encontró el archivo de fondo.mp3")

# Risa o efectos puntuales (una sola vez)
def reproducir_audio_autoplay(ruta):
    try:
        with open(ruta, "rb") as audio_file:
            audio_bytes = audio_file.read()
            audio_base64 = base64.b64encode(audio_bytes).decode()
            audio_html = f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3" />
            </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ No se encontró el archivo de efecto.mp3")

# ------------------------ ESTILOS Y ENCABEZADO ------------------------

# Fondo visual
fondo_con_base64("static/images/fondo.jpg")

# Título y subtítulo
st.markdown("<h1 style='color:white; text-align:center;'>🎮 El Oráculo Tóxico</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:white; text-align:center;'>🧙 El Maestro Zervantes te revela tu destino</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>By Xibalbá Games</h4>", unsafe_allow_html=True)

# Instrucciones
st.markdown("""
<div style='background-color:rgba(0,0,0,0.7); padding:1em; border-radius:10px; color:white; font-size:1.1em'>
<b>Instrucciones:</b><br>
Si en tu <i>primer intento</i> aparece la predicción <b style='color:#00ccff'>“¡¡ESTÁS DE SUERTE!! pide un deseo y te lo concederé.”</b><br>
Tu deseo se cumplirá sin consecuencias…<br>
Pero si fallas, <b>todo lo que el Maestro Zervantes decrete en cada intento será inevitable.</b><br>
<b>Juega si te atreves.</b>
</div>
""", unsafe_allow_html=True)

# Estilo de botón
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #990000;
        color: white;
        border: none;
        padding: 0.75em 1.5em;
        font-weight: bold;
        font-size: 1em;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------ BOTÓN PRINCIPAL ------------------------

if st.button("Consultar el destino"):
    reproducir_audio_fondo_autoplay("static/audio/fondo.mp3")  # Solo después de clic
    mensaje = random.choice(predicciones)

    if "ESTÁS DE SUERTE" in mensaje.upper():
        st.markdown(f"<h3 style='color:#00ccff'>{mensaje}</h3>", unsafe_allow_html=True)
        st.success("¡Tu deseo será concedido! Escoge bien...")
    else:
        st.markdown(f"<h3 style='color:white'>{mensaje}</h3>", unsafe_allow_html=True)
        reproducir_audio_autoplay("static/audio/risa.mp3")

    st.image("static/images/lemur.gif", caption="El universo te responde...", use_container_width=True)
