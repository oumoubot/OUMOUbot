import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="OUMOU - Assistante Malienne", page_icon="🇲🇱")
st.title("🇲🇱 OUMOU - Ton Assistante Malienne")
st.write("An bɛ taa! Je suis là")

# MODÈLE QUI NE DEMANDE PAS DE CLÉ
client = InferenceClient("microsoft/Phi-3-mini-4k-instruct")

prompt = st.text_input("Écris ici:")

if st.button("Envoyer"):
    if prompt:
        with st.spinner("OUMOU réfléchit..."):
            prompt_final = f"Tu es OUMOU, assistante malienne. Réponds en français et un peu bambara. Sois gentille et courte. Question: {prompt}"
            response = client.text_generation(prompt_final, max_new_tokens=200)
            st.success(f"**OUMOU:** " + response)
