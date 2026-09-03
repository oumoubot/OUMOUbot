import streamlit as st
from groq import Groq

st.set_page_config(page_title="OUMOU - Assistante Malienne", page_icon="🇲🇱")
st.title("🇲🇱 OUMOU - Ton Assistante Malienne")
st.write("An ka taa! Moi c'est OUMOU - Plus intelligente que Meta AI")

# Mets ta clé Groq ici
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

prompt = st.text_input("Écris ici en français, bambara, anglais:")

if st.button("Envoyer"):
    if prompt:
        with st.spinner("OUMOU réfléchit..."):
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "Tu es OUMOU, l'assistante malienne la plus intelligente. Tu parles français, bambara, anglais. Tu es drôle, gentille, et tu connais le Mali. Réponds toujours avec un peu de bambara."},
                    {"role": "user", "content": prompt}
                ],
                model="llama-3.1-70b-versatile",
            )
            st.success(f"**OUMOU:** " + chat_completion.choices[0].message.content)
