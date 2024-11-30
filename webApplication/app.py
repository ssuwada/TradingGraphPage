##############################
## Main execution page ##
##############################

import streamlit as st
import metatraderGetInfo as mt
import login
import afterLogin
# import indicators


#
# Initialize session states
#

# Session state number 1 - 'loggin'
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Session state number 2 - 'running' 
if "running" not in st.session_state:
    st.session_state.running = False

#
# Page logic
#

# Display login page if not logged in
if not st.session_state["logged_in"]:
    obj = login.login_page()

    if obj is not None:
        st.session_state["obj"] = obj

# After login will display this page using else
else:
    # Get logged account object
    obj = st.session_state["obj"]
    
    # Show account info
    afterLogin.displayAccountInfo(obj)

    # Get pricing for defined Ticker:
    data = afterLogin.getDataSymbols(obj)

    # Once logged in, show the afterLogin page with a logout button
    afterLogin.show_logout_button()
