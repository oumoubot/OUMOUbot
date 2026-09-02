import streamlit as st

st.set_page_config(page_title="OUMOU BOT V3", page_icon="🤖", layout="centered")

# BEAUTÉ DU SITE
st.markdown("""
<style>
.stApp { 
    background: linear-gradient(135deg, #006633 0%, #FCD116 50%, #CE1126 100%);
}
.logo { text-align: center; padding-top: 30px; }
.title { text-align: center; color: white; font-size: 40px; font-weight: bold; text-shadow: 2px 2px 4px black; }
.subtitle { text-align: center; color: white; font-size: 18px; margin-bottom: 30px; }
.stButton>button { 
    width: 100%; height: 60px; font-size: 20px; 
    background-color: #25D366; color: white; 
    border-radius: 15px; border: none; font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# LOGO
st.markdown('<div class="logo">', unsafe_allow_html=True)
st.image("IMG-20260901-WA9281.jpg", width=220)
st.markdown('</div>', unsafe_allow_html=True)

# TITRE
st.markdown('<p class="title">OUMOU BOT V3</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Assistant pour Touts</p>', unsafe_allow_html=True)

st.write("")
st.write("")

# BOUTON WHATSAPP
st.link_button("💬 PARLER À OUMOU SUR WHATSAPP", "https://wa.me/22368497540")

st.markdown("---")
st.markdown("<center style='color:white'>Made with ❤️ au Mali</center>", unsafe_allow_html=True)
