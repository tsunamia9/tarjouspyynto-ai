import streamlit as st
from google import genai

st.set_page_config(
    page_title="Tarjouspyyntö AI",
    page_icon="📄",
)

st.title("📄 Tarjouspyyntö AI")
st.write("Liitä tarjouspyyntö alle, niin AI analysoi sen.")

request = st.text_area(
    "Tarjouspyyntö",
    height=300,
    placeholder="Liitä asiakkaan tarjouspyyntö tähän..."
)

if st.button("Analysoi tarjouspyyntö"):
    if not request.strip():
        st.warning("Syötä ensin tarjouspyyntö.")
    else:
        client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        prompt = f"""
Analysoi seuraava yrityksen tarjouspyyntö.

Kerro selkeästi:

1. Mitä asiakas tarvitsee?
2. Mitkä ovat tärkeimmät vaatimukset?
3. Mitä tietoja tarjouspyynnöstä puuttuu?
4. Mitä yrityksen pitäisi ottaa huomioon tarjousta tehdessä?
5. Tee lopuksi lyhyt ehdotus vastaukseksi asiakkaalle.

Tarjouspyyntö:

{request}
"""

        with st.spinner("AI analysoi tarjouspyyntöä..."):
            response = client.interactions.create(
                model="gemini-3-flash-preview",
                input=prompt
            )

        st.subheader("AI:n analyysi")
        st.write(response.output_text)
