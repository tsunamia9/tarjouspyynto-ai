import streamlit as st

st.set_page_config(
    page_title="Tarjouspyyntö AI",
    page_icon="📄",
)

st.title("📄 Tarjouspyyntö AI")
st.write("Liitä tarjouspyyntö alle, niin työkalu analysoi sen.")

request = st.text_area(
    "Tarjouspyyntö",
    height=300,
    placeholder="Esim. Tarvitsemme verkkosivut 10 hengen rakennusyritykselle..."
)

if st.button("Analysoi tarjouspyyntö"):
    if not request.strip():
        st.warning("Syötä ensin tarjouspyyntö.")
    else:
        st.subheader("Analyysi")
        st.write("Tarjouspyyntö vastaanotettu.")
        st.write(f"**Tekstin pituus:** {len(request)} merkkiä")
