import streamlit as st
from io import StringIO
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# Login section
login_option = st.sidebar.radio('Login/Signup', ('Login', 'Signup'))

if login_option == 'Login':
    with st.sidebar.form('Login'):
        st.write('Login here...')
        username = st.text_input('Username:')
        password = st.text_input('Passowrd:', type='password')
        submitted = st.form_submit_button('Login')
        if submitted:
            pass
else:
    with st.sidebar.form('Signup'):
        st.write('Signup here...')
        username = st.text_input('Username:')
        password = st.text_input('Passowrd:', type='password')
        email = st.text_input('Email:')
        submitted = st.form_submit_button('Signup')
        if submitted:
            pass

# Title
st.title(':computer: GP Dashboard')

# Metric section
st.metric(label='Telegram Group Members', value='35', delta='3')

# JSON reader section
with st.expander('Upload a json file'):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)

        data = json.loads(string_data)
        st.json(data)

# Statistics section
with st.expander('Statistics'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)

# User profile details section
with st.expander('User Profile:'):
    col1, col2 = st.columns(2)
    col1.text_input('Name:')
    col2.text_input('Location:')
    st.camera_input('Camera Input', key='camera_input')
