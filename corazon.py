import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Un corazón para ti 💗", page_icon="💖", layout="centered"
)

# DISEÑO
st.markdown(
    """
<style>
.stApp {
    background: radial-gradient(circle at center, #301329, #100914 85%);
    color: white;
}

.titulo {
    text-align: center;
    color: #ff80ab;
    font-size: 32px;
    font-weight: bold;
}

.mensaje {
    text-align: center;
    color: #ffd1e2;
    font-size: 20px;
}

.stButton button {
    background: linear-gradient(135deg, #e84383, #c2185b);
    color: white;
    border-radius: 25px;
    border: 1px solid #ff80ab;
    padding: 12px 22px;
    width: 100%;
    font-weight: bold;
}
</style>
""",
    unsafe_allow_html=True,
)


# CORAZÓN FORMADO SOLO POR EL CONTORNO DE FRASES
def mostrar_corazon():
    components.html(
        """
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        padding: 0;
        background: transparent;
        overflow: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: Arial, sans-serif;
    }

    #heart {
        position: relative;
        width: 100%;
        max-width: 500px;
        height: 410px;
        margin: auto;
        transform-origin: center;
    }

    .word {
        position: absolute;
        white-space: nowrap;
        font-size: 10px;
        font-weight: bold;
        opacity: 0;
        transform: translate(-50%, -50%) scale(0.2);
        transition:
            left 1.2s cubic-bezier(.2,.8,.2,1),
            top 1.2s cubic-bezier(.2,.8,.2,1),
            opacity 0.6s ease,
            transform 1.2s ease;
        text-shadow: 0 0 6px currentColor;
    }

    .word.settled {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1);
    }

    #heart.beating {
        animation: heartbeat 1.5s ease-in-out infinite;
    }

    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        15% { transform: scale(1.045); }
        30% { transform: scale(1); }
        45% { transform: scale(1.025); }
        60% { transform: scale(1); }
    }
    </style>
    </head>

    <body>

    <div id="heart"></div>

    <script>

    const phrases = [
        "Te quiero ",
        "I love you ",
        "Je t'aime ",
        "Ich liebe dich ",
        "Ti amo ",
        "Suki da yo ",
        "Te amo ",
        "Saranghae ",
        "Mahal kita ",
        "Kocham cię ",
        "Я тебя люблю ",
        "Minä rakastan sinua "
    ];

    const colors = [
        "#ff1744",
        "#ff4081",
        "#ff80ab",
        "#f50057",
        "#e040fb",
        "#ff5252",
        "#ec407a",
        "#ffb6c1"
    ];

    const heart = document.getElementById("heart");

    const width = 500;
    const height = 410;
    const centerX = width / 2;
    const centerY = height / 2 - 10;

    let positions = [];

    // SÓLO EL CONTORNO (Puntos del borde con mayor definición)
    let numBoundary = 135;
    for (let i = 0; i < numBoundary; i++) {
        let t = (i / numBoundary) * Math.PI * 2;
        let x = 16 * Math.pow(Math.sin(t), 3);
        let y = -(13 * Math.cos(t) - 5 * Math.cos(2*t) - 2 * Math.cos(3*t) - Math.cos(4*t));
        positions.push({
            x: centerX + x * 11.5,
            y: centerY + y * 11.5
        });
    }

    // CREAR LAS FRASES PARA EL BORDE
    positions.forEach((pos, i) => {
        const word = document.createElement("div");
        word.className = "word";
        word.textContent = phrases[i % phrases.length];
        word.style.color = colors[i % colors.length];

        // Posición inicial aleatoria en los bordes
        let startX = 10 + ((i * 37) % 80);
        let startY = 10 + ((i * 53) % 80);
        word.style.left = startX + "%";
        word.style.top = startY + "%";

        heart.appendChild(word);

        // Mover a su posición final en el contorno
        setTimeout(() => {
            word.style.left = (pos.x / width * 100) + "%";
            word.style.top = (pos.y / height * 100) + "%";
            word.classList.add("settled");
        }, 150 + i * 25);
    });

    // Latido al terminar
    setTimeout(() => {
        heart.classList.add("beating");
    }, 150 + positions.length * 25 + 1000);

    </script>

    </body>
    </html>
    """,
        height=430,
        scrolling=False,
    )


# ESTADO
if "pantalla" not in st.session_state:
    st.session_state.pantalla = 1


# PANTALLA 1: MENSAJE INICIAL
if st.session_state.pantalla == 1:
    st.markdown(
        "<h1 class='titulo'>💌 Te quiero decir algo...</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p class='mensaje'>Hay algo que quiero que veas. ❤️</p>",
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button("💗 Ver mi mensaje 💗"):
        st.session_state.pantalla = 2
        st.rerun()


# PANTALLA 2: CORAZÓN ANIMADO
elif st.session_state.pantalla == 2:
    st.markdown(
        "<h1 class='titulo'>Para ti... ❤️</h1>", unsafe_allow_html=True
    )

    st.markdown(
        "<p class='mensaje'>Cada palabra significa lo mismo...</p>",
        unsafe_allow_html=True,
    )

    mostrar_corazon()

    st.markdown(
        "<h2 class='titulo'>¿Me quieres? 🥺💕</h2>", unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("¡Sí, muchísimo! 🥰"):
            st.session_state.pantalla = 3
            st.rerun()

    with col2:
        if st.button("Obvio que sí 💖"):
            st.session_state.pantalla = 3
            st.rerun()


# PANTALLA 3: RESPUESTA FINAL
elif st.session_state.pantalla == 3:
    st.markdown(
        "<h1 class='titulo'>¡Yo también te quiero muchísimo! 💘</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p class='mensaje'>Eres de lo mejor que me ha pasado en la vida. ✨</p>",
        unsafe_allow_html=True,
    )

    mostrar_corazon()

    st.markdown(
        "<h3 class='titulo'>Para ti con todo mi corazón 💌</h3>",
        unsafe_allow_html=True,
    )

    if st.button("🔄 Volver a empezar"):
        st.session_state.pantalla = 1
        st.rerun()
