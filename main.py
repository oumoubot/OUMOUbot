import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="OUMOU", page_icon="🤖")
st.title("🤖 OUMOU - Assistante Malienne")
st.write("I ni cé! Ne b'i togo fô")

try:
    api_key = st.secrets["GOOGLE_API_KEY"]
except:
    st.error("⚠️ Va dans Streamlit > Settings > Secrets")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

prompt = st.text_input("Écris ici:")
if st  if st.button("Envoyer"):
    if prompt:
        with st.spinner("OUMOU réfléchit..."):
            response = model.generate_content(
                f"Tu es OUMOU, assistante malienne. Réponds en français et bambara. "
                f"Sois courte et gentille. Question: {prompt}"
            )
            st.success(f"**OUMOU:** " + response.text)   
