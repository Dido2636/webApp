import streamlit as st

#Afficher un titre
st.title('Hello world')

#Afficher des sous-titre
st.subheader('Cest un sous-titre')

#Afficher du texte
st.write('Ceci est un texte')

#Champs de saisie que nous avons mis dans une variable 
user_input = st.text_input('Ceci est champs de saisie')

#Afficher à l'écran
st.write(user_input)

#Afficher une image
st.image('https://www.eemi.com/wp-content/themes/eemi/assets/imgs/logo-eemi.svg')

#creer un formulaire
with st.form('Form1'):

    #on demande à l'utilisateur son nom
    user_name = st.text_input('Tape you name:')

    #Boutton
    if st.form_submit_button("Send"):
        st.write(user_name)
