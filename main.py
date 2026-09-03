import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="OUMOU", page_icon="🤖", layout="centered")

st.title("🤖 OUMOU - Assistante Bambara")
st.markdown("I ni cé Adama ! Ne b'i togo fô")

# Clé API
api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("⚠️ Mets GOOGLE_API_KEY dans Settings > Secrets")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Formulaire au lieu de chat_input
with st.form(key="form_oumou", clear_on_submit=True):
    prompt = st.text_input("Écris ici en français ou bambara...")
    submit_button = st.form_submit_button(label="Envoyer")

if submit_button and prompt:
    with st.spinner("OUMOU réfléchit..."):
        response = model.generate_content(
            f"Tu es OUMOU, une assistante malienne gentille. Tu parles bambara et français. "
            f"Si on te parle en bambara, réponds en bambara. Sois courte. "
            f"Question: {prompt}"
        )
        st.success("**OUMOU:** " + response.text)
