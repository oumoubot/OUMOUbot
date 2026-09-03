import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="OUMOU", page_icon="🤖")

st.title("🤖 OUMOU - Assistante Bambara")
st.write("I ni cé Adama ! Ne b'i togo fô")

# Clé API
api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY manquant dans Secrets")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Zone de chat
if prompt := st.chat_input("Écris ici en français ou bambara..."):
    st.write(f"**Toi:** {prompt}")
    
    with st.spinner("OUMOU réfléchit..."):
        response = model.generate_content(
            f"Tu es OUMOU, une assistante malienne. Tu parles bambara et français. "
            f"Si on te parle en bambara, réponds en bambara. "
            f"Question: {prompt}"
        )
        st.write(f"**OUMOU:** {response.text}")
