import streamlit as st
import streamlit_authenticator as stauth
#import yaml


# Authentication function #https://github.com/naashonomics/pandas_templates/blob/master/login.py
def login():
    names = ['Yosua 🐷', '🏄']
    usernames = ['yosua', 'kamal']
    passwords = ['cerdo', 'puerco']

    hashed_passwords = stauth.Hasher(passwords).generate()
    authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                        'some_cookie_name', 'some_signature_key', cookie_expiry_days=1)
    name, authentication_status, username = authenticator.login('Login', 'main')
    
    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{name}*')
        return True
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username (🐷) and password (💰)')
    return False