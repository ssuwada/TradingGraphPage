##############################
## Credentials & login page ##
##############################

import streamlit as st
from metatraderGetInfo import metaTrader as mt


def login_page():
    st.title("Please provide credentials")

    # Input fields for login
    username = st.text_input("Username")
    password = str(st.text_input("Password", type="password"))
    server = str(st.selectbox('Server selection', options=('MetaQuotes-Demo', 'MT1')))

    # Check if input is not empty and is a valid integer

    try:
        username_conv = int(username)  # Convert to integer
        print(f"Converted username to: {username_conv}")
        username = username_conv
    except ValueError:
        st.warning("Please enter a valid numeric username.")

    # Logic about loggin and login button

    obj = login_logic(username, password, server)
    if obj is not None:
        return obj
    return None

def login_logic(username, password, server):

    if st.button("Login"):
        obj = mt(username, password, server)
        print(obj)
        loginReturn = obj.initializeMT(username, password, server)

        if not loginReturn:
            st.error("Invalid username or password")
            st.session_state["logged_in"] = False
            return None
        else:
            st.session_state["logged_in"] = True
            st.success("Login successful!")
            return obj


# login_logic(87838469, '@a5bTnOx', 'MetaQuotes-Demo')