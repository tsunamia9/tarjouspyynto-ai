import streamlit as st
from google import genai

st.set_page_config(
    page_title="Tarjouspyyntö AI",
    page_icon="📄",
    layout="wide",
)

# ---------- CUSTOM CSS ----------

st.markdown("""
<style>

/* Background */
.stApp {
    background: #f4f6f8;
}

/* Main container */
.block-container {
    max-width: 1100px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

/* Header */
.hero {
    background: #ffffff;
    padding: 2.5rem;
    border-radius: 18px;
    border: 1px solid #e2e6ea;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
}

.hero h1 {
    font-size: 2.8rem;
    margin: 0;
    color: #111827;
}

.hero p {
    color: #6b7280;
    font-size: 1.1rem;
    margin-top: 0.7rem;
}

/* Input card */
.input-card {
    background: #ffffff;
    padding: 1.5rem;
    border-radius: 16px;
    border: 1px solid #e2e6ea;
    box-shadow: 0 4px 20px rgba(0,0,0,0.03);
}

/* Text area */
textarea {
    background: #ffffff !important;
    border-radius: 12px !important;
}

/* Analyze button */
.stButton > button {
    background: #2563eb;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #1d4ed8;
    transform: translateY(-1px);
}

/* Result */
.result-card {
    background: #ffffff;
    padding: 2rem;
    border-radius: 16px;
    border: 1px solid #e2e6ea;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    margin-top: 1.5rem;
}

/* Divider */
hr {
    border-color: #e5e7eb;
}

</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------

st.markdown("""
<div class="hero">
    <h1>📄 Tarjouspyyntö AI</h1>
    <p>
        Muuta asiakkaan tarjouspyyntö nopeasti
        selkeäksi analyysiksi ja vastausluonnokseksi.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------- INPUT ----------

st.markdown("""
<div class="input-card">
<h3>Tarjouspyyntö</h3>
<p style="color:#6b7280;">
Liitä asiakkaan tarjouspyyntö alla olevaan kenttään.
</p>
</div>
""", unsafe_allow_html=True)

request = st.text_area(
    "Tarjouspyyntö",
    height=300,
    placeholder=(
        "Esimerkiksi:\n\n"
        "Hei,\n"
        "Tarvitsemme yrityksellemme uudet verkkosivut..."
    ),
    label_visibility="collapsed",
)

st.write("")

analyze = st.button(
    "🚀  Analysoi tarjouspyyntö",
    type="primary",
    use_container_width=True,
)


# ---------- AI ----------

if analyze:

    if not request.strip():
        st.warning("Liitä tarjouspyyntö ennen analysointia.")

    else:

        client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        prompt = f"""
Olet B2B-myyntiä ja tarjouspyyntöjä käsittelevä asiantuntija.

Analysoi seuraava tarjouspyyntö.

Tee analyysi näillä otsikoilla:

## Asiakkaan tarve
Kerro lyhyesti mitä asiakas haluaa.

## Tärkeimmät vaatimukset
Listaa tarjouspyynnön tärkeimmät vaatimukset.

## Puuttuvat tiedot
Listaa tiedot, jotka pitäisi selvittää ennen tarjouksen tekemistä.

## Myynnillinen arvio
Kerro lyhyesti, mitä tässä kannattaa myydä ja mihin kannattaa kiinnittää huomiota.

## Ehdotus vastaukseksi
Kirjoita valmis, ammattimainen sähköpostivastaus asiakkaalle.
Älä keksi hintaa tai ominaisuuksia, joita tarjouspyynnössä ei mainita.

Tarjouspyyntö:

{request}
"""

        with st.spinner("Analysoidaan tarjouspyyntöä..."):

            response = client.interactions.create(
                model="gemini-3-flash-preview",
                input=prompt
            )

        st.markdown("""
        <div class="result-card">
        <h2>🤖 AI:n analyysi</h2>
        """, unsafe_allow_html=True)

        st.markdown(response.output_text)

        st.markdown("</div>", unsafe_allow_html=True)
