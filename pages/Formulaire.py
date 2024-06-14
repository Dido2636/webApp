import streamlit as st

#Demandez à l’utilisateur son nom, son prénom, son âge, son niveau d’étude [Sans diplôme, BAC, BAC+2, BAC+5, BAC+8].


#creation du formulaire
with st.form('Formulaire d inscription'):
    user_name = st.text_input('Nom')

    user_fistname = st.text_input('Prénom')

    number = st.select_slider(
    "Quel est voytre age",
    options= range(18, 99))
   
    
    option = st.selectbox(
    "Quel est votre niveau d'étude",
    ("Sans diplôme", "BAC", "BAC+2", "BAC+5", "BAC+8"))

    submit_data = st.form_submit_button("Soumettre")

    if submit_data:
        age = number
        if age < 18:
            st.write("Vous êtes mineur")
        else:
            st.write("Vous êtes majeur")
        
        
st.sidebar.write(user_name, user_fistname,)

st.sidebar.write('https://github.com/Dido2636?tab=repositories')