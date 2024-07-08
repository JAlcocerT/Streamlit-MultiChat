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

# def load_credentials():
#     # Load the YAML file
#     with open('credentials.yml', 'r') as file:
#         credentials = yaml.safe_load(file)
#     return credentials

# def init_authenticator():
#     credentials = load_credentials()
    
#     # Extract the cookie settings from the loaded credentials
#     cookie_config = credentials.get('cookie', {})
    
#     # Initialize the authenticator
#     authenticator = stauth.Authenticate(
#         credentials['credentials'],
#         cookie_config['name'],
#         cookie_config['key'],
#         cookie_expiry_days=cookie_config.get('expiry_days', 30)
#     )
#     return authenticator

# def login(authenticator):
#     name, authentication_status, username = authenticator.login("Login", "main")
#     return name, authentication_status, username



# import streamlit as st
# import streamlit_authenticator as stauth

# def init_authenticator():
#     # Define your user credentials here
#     usernames = {
#         "Yosua": {
#             "name": "yosua",
#             "hashed_password": "$2b$12$P5T0hO/bSQ3Y8fCqcW18iOvfazxM995AoVlcCVmxijysc4mjvn6am", #hashed password with hash_password.py
#         }
#     }

#     # Initialize the authenticator
#     authenticator = stauth.Authenticate(users, "my_cookie", "my_signature_key", cookie_expiry_days=30)
#     return authenticator

# def login(authenticator):
#     name, authentication_status, username = authenticator.login("Login", "main")
#     return name, authentication_status, username