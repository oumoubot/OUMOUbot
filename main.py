import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
from PIL import Image
import io

st.set_page_config(page_title="OUMOU - IA du Mali", page_icon="🇲🇱")

# 1. CONNEXION À GEMINI
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🇲🇱 OUMOU - IA du Mali")
st.write("I ni cé! Je parle Bambara, Français. Envoie texte, vocal ou photo")

# 2. ZONE DE CHAT
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. UPLOAD PHOTO
photo = st.file_uploader("📸 Envoie une photo à OUMOU", type=["jpg", "png"])

# 4. BOUTON MICRO
if st.button("🎤 Parler"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Ka dòn... Parle maintenant")
        audio = r.listen(source)
    try:
        texte = r.recognize_google(audio, language="fr-FR") # on met fr car bm est rare
        st.session_state.messages.append({"role": "user", "content": texte})
    except:
        st.error("N'a pas compris")

# 5. ZONE TEXTE
prompt = st.chat_input("Écris à OUMOU ici...")

# 6. TRAITEMENT
input_data = prompt
if photo:
    input_data = [prompt, Image.open(photo)]
    st.image(photo)

if prompt or photo:
    st.session_state.messages.append({"role": "user", "content": str(input_data)})
    
    response = model.generate_content(input_data)
    reponse_texte = response.text
    st.session_state.messages.append({"role": "assistant", "content": reponse_texte})
    
    # 7. OUMOU PARLE
    tts = gTTS(text=reponse_texte, lang='fr') # 'fr' marche mieux que 'bm'
    tts.save("reponse.mp3")
    st.audio("reponse.mp3")

# 8. AFFICHER L'HISTORIQUE
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
