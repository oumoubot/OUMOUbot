import streamlit as st

# CONFIG DE LA PAGE
st.set_page_config(
    page_title="OUMOU BOT V3",
    page_icon="🇲🇱",
    layout="centered"
)

# COULEURS MALI
st.markdown("""
<style>
    .main {background-color: #F0F2F6;}
    h1 {color: #14B53A;} /* VERT */
    h2 {color: #FCD116;} /* JAUNE */
    h3 {color: #CE1126;} /* ROUGE */
</style>
""", unsafe_allow_html=True)

# TITRE
st.title("🇲🇱 OUMOU BOT V3")
st.header("L'IA du Mali")
st.write("Salut Adama ! Ton bot est en ligne et il marche.")

# CHAT
user_input = st.text_input("Pose ta question ici:")
if user_input:
    st.success(f"Tu as dit: {user_input}")
    st.info("Bientôt je vais répondre avec l'IA Gemini")
