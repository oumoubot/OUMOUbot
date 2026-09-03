import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="OUMOU BOT V3", page_icon="🇲🇱", layout="centered")
st.markdown("""<style>h1 {color: #14B53A;} h2 {color: #FCD116;} h3 {color: #CE1126;}</style>""", unsafe_allow_html=True)

st.title("🇲🇱 OUMOU BOT V3")
st.write("L'IA du Mali - Pose-moi n'importe quelle question")

# CONNEXION À GEMINI
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Écris ta question ici..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("OUMOU réfléchit..."):
            response = model.generate_content(f"Tu es OUMOU BOT V3, l'IA du Mali. Sois gentil, utile et réponds en français. Question: {prompt}")
            st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
