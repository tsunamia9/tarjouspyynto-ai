import streamlit as st
from google import genai

st.set_page_config(
    page_title="Tarjouspyyntö AI",
    page_icon="📄",
    layout="centered",
)

st.title("📄 Tarjouspyyntö AI")
st.write("Analysoi yrityksen tarjouspyyntö ja luo valmis vastausluonnos.")

st.divider()

request = st.text_area(
    "Tarjouspyyntö",
    height=300,
    placeholder="Liitä asiakkaan tarjouspyyntö tähän..."
)

if st.button("Analysoi tarjouspyyntö", type="primary"):

    if not request.strip():
        st.warning("Syötä ensin tarjouspyyntö.")

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

        st.subheader("🤖 AI:n analyysi")
        st.markdown(response.output_text)
