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

/* ---------- Background ---------- */

.stApp {
    background: #102a24;
}

.block-container {
    max-width: 1100px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}


/* ---------- Header ---------- */

.hero {
    background: #173a31;
    padding: 2.5rem;
    border-radius: 18px;
    border: 1px solid #285447;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}

.hero h1 {
    font-size: 2.8rem;
    margin: 0;
    color: #ffffff;
}

.hero p {
    color: #b8cbc5;
    font-size: 1.1rem;
    margin-top: 0.7rem;
}


/* ---------- Input card ---------- */

.input-card {
    background: #ffffff;
    padding: 1.5rem;
    border-radius: 16px;
    border: 1px solid #dfe5e2;
    box-shadow: 0 8px 25px rgba(0,0,0,0.12);
}

.input-card h3 {
    color: #173a31;
    margin-bottom: 0.3rem;
}

.input-card p {
    color: #66736f;
}


/* ---------- Text area ---------- */

textarea {
    background: #ffffff !important;
    color: #17201d !important;
    border-radius: 12px !important;
    border: 1px solid #d8dfdc !important;
}

textarea:focus {
    border-color: #2f8f6b !important;
}


/* ---------- Analyze button ---------- */

.stButton > button {
    background: #2f8f6b;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.8rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    transition: 0.2s;
    box-shadow: 0 5px 15px rgba(47,143,107,0.25);
}

.stButton > button:hover {
    background: #26785a;
    color: white;
    transform: translateY(-1px);
}


/* ---------- Result card ---------- */

.result-card {
    background: #ffffff;
    color: #17201d;
    padding: 2rem;
    border-radius: 16px;
    border: 1px solid #dfe5e2;
    box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    margin-top: 1.5rem;
}

.result-card h2 {
    color: #173a31;
}


/* ---------- Divider ---------- */

hr {
    border-color: #285447;
}


/* ---------- Warning ---------- */

.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------

st.markdown("""
<div class="hero">
    <h1>Tarjouspyyntö AI</h1>
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
    <p>
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


# ---------- BUTTON ----------

analyze = st.button(
    "Analysoi tarjouspyyntö",
    type="primary",
    use_container_width=True,
)


# ---------- AI ANALYSIS ----------

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

Älä keksi hintaa tai ominaisuuksia,
joita tarjouspyynnössä ei mainita.

Tarjouspyyntö:

{request}
"""

        with st.spinner("Analysoidaan tarjouspyyntöä..."):

            response = client.interactions.create(
                model="gemini-3-flash-preview",
                input=prompt
            )


        # ---------- RESULT ----------

        st.markdown("""
        <div class="result-card">
            <h2>🤖 AI:n analyysi</h2>
        """, unsafe_allow_html=True)

        st.markdown(response.output_text)

        st.markdown("""
        </div>
        """, unsafe_allow_html=True)
