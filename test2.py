import streamlit as st
def change():
    if option == 'Email':
        st.write('EmailEmail')
    elif option=='Home phone':
        st.write('HomeHome')
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

if option == 'Email':
    st.write('EmailEmail')
elif option=='Home phone':
    st.write('HomeHome')
st.write('You selected:', option)