import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="OUMOU - Assistante Malienne", page_icon="🇲🇱")

st.title("🇲🇱 OUMOU - Ton Assistante Malienne")
st.write("An ka taa! Pose moi une question en français ou en bambara")

# Sécurité: Vérifie si la clé existe
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    st.error("⚠️ Va dans Streamlit > Settings > Secrets et ajoute GOOGLE_API_KEY")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Zone de texte
prompt = st.text_input("Écris ici:")

if st.button("Envoyer"):
    if prompt:
        with st.spinner("OUMOU réfléchit..."):
            response = model.generate_content(
                f"Tu es OUMOU, assistante malienne. Réponds en français et bambara. "
                f"Sois courte, gentille et drôle. Question: {prompt}"
            )
            st.success(f"**OUMOU:** " + response.text)
    else:
        st.warning("Écris quelque chose d'abord")
