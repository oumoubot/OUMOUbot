import streamlit as st
import random

st.set_page_config(page_title="OUMOU - Assistante Malienne", page_icon="🇲🇱")
st.title("🇲🇱 OUMOU - Ton Assistante Malienne")
st.write("An ka taa! Moi c'est OUMOU")

# Réponses de OUMOU en français + bambara
reponses = {
    "salut": ["I ni cé! Ça va? 😊", "Aw ni cè! Comment tu vas?"],
    "comment": ["N bɛ kɛnɛya. Et toi? Je vais bien", "Je vais bien alhamdoulilah. Et toi?"],
    "aide": ["N bɛ se ka dɛmɛ i la. Que veux-tu? Je peux t'aider", "Dis moi ce qu'il faut faire"],
    "merci": ["Tɛ i kɛ! De rien", "Aw ni ce. Avec plaisir"],
    "default": ["Ayiwa, n ma famu kosɛbɛ. Peux-tu répéter?", "N tɛ a faamu. Explique moi encore stp"]
}

prompt = st.text_input("Écris ici:")

if st.button("Envoyer"):
    if prompt:
        prompt_lower = prompt.lower()
        reponse = random.choice(reponses["default"])
        
        if "salut" in prompt_lower or "cé" in prompt_lower:
            reponse = random.choice(reponses["salut"])
        elif "comment" in prompt_lower or "kɛnɛ" in prompt_lower:
            reponse = random.choice(reponses["comment"])
        elif "aide" in prompt_lower or "dɛmɛ" in prompt_lower:
            reponse = random.choice(reponses["aide"])
        elif "merci" in prompt_lower or "tɛ" in prompt_lower:
            reponse = random.choice(reponses["merci"])
            
        st.success(f"**OUMOU:** {reponse}")
