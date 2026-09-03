import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="OUMOU - Assistante Malienne", page_icon="🇲🇱")
st.title("🇲🇱 OUMOU - Ton Assistante Malienne")

# Client gratuit HuggingFace
client = InferenceClient("meta-llama/Llama-3.1-8B-Instruct")

prompt = st.text_input("Écris ici:")

if st.button("Envoyer"):
    if prompt:
        with st.spinner("OUMOU réfléchit..."):
            messages = [{"role": "user", "content": f"Tu es OUMOU, assistante malienne. Réponds en français et bambara. Sois courte. Question: {prompt}"}]
            response = client.chat_completion(messages, max_tokens=200)
            st.success(f"**OUMOU:** " + response.choices[0].message.content)
