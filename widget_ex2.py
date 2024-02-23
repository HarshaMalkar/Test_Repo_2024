import streamlit as st

st.title('Making a Button') 
result =st.button('click here') 
st.write(result)

if result:
     st.write(':smile:')
