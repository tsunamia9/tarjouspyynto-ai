import streamlit as st
from google import genai

st.set_page_config(
    page_title="Tarjouspyyntö AI",
    page_icon="📄",
    layout="wide",
)

# ---------- STYLE ----------

st.markdown("""
<style>
    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    .hero {
        padding: 2rem 0 1.5rem 0;
    }

    .hero h1 {
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
    }

    .hero p {
        font-size: 1.15rem;
        color: #666;
    }

    .section-title {
        font-size: 1.3rem;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }

    .result-box {
        padding: 1.5rem;
        border: 1px solid #e5e5e5;
        border-radius: 12px;
        background: #fafafa;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------

st.markdown("""
<div class="hero">
    <h1>📄 Tarjouspyyntö AI</h1>
    <p>
        Muuta asiakkaan tarjouspyyntö selkeäksi analyysiksi
        ja valmiiksi vastausluonnokseksi.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()


# ---------- INPUT ----------

st.markdown(
    '<div class="section-title">Tarjouspyyntö</div>',
    unsafe_allow_html=True
)

request = st.text_area(
    "",
    height=300,
    placeholder=(
        "Liitä asiakkaan tarjouspyyntö tähän...\n\n"
        "Esimerkiksi:\n"
        "Tarvitsemme uudet verkkosivut yrityksellemme..."
    ),
    label_visibility="collapsed",
)

st.write("")

analyze = st.button(
    "🚀 Analysoi tarjouspyyntö",
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

        st.divider()

        st.markdown(
            '<div class="section-title">🤖 AI:n analyysi</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="result-box">',
            unsafe_allow_html=True
        )

        st.markdown(response.output_text)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )
