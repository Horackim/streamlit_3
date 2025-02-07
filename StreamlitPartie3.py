import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes =\
{'usernames': 
    {'Julien': 
        {'name': 'julien',
        'password': 'julienMDP',
        'email': 'toto@toto.com',
        'failed_login_attemps': 0, # Sera géré automatiquement
        'logged_in': False, # Sera géré automatiquement
        'role': 'utilisateur'
        },
        
    'root': 
        {'name': 'root',
        'password': 'rootMDP',
        'email': 'admin@gmail.com',
        'failed_login_attemps': 0, # Sera géré automatiquement
        'logged_in': False, # Sera géré automatiquement
        'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "kikoololasv", # Le nom du cookie, un str quelconque
    "kikoololasv", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

st.write("login : julien")
st.write("mdp : julienMDP")

authenticator.login()
def accueil():
    st.title("Bienvenu sur la page de Julien")
    st.image("https://raw.githubusercontent.com/Horackim/streamlit_3/594282bff286474785b163150c738281eab58b2e/familyguy.jpg")

def album():
    st.title("Bienvenue sur mon album photo")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")


if st.session_state["authentication_status"]:
    with st.sidebar:
        authenticator.logout("Déconnexion")
        st.write(f"Bienvenue *{st.session_state["name"]}*")
        selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )
    if selection == "Accueil":
        accueil()
    elif selection == "Photos":
        album()
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')
