import streamlit as st
from snowflake.snowpark import Session
from streamlit_dbtree import streamlit_dbtree

st.title('❄️ Snowflake DB Tree')

conn = st.connection("snowflake")

value = streamlit_dbtree(conn,key="snowflake")
if value is not None:
    for sel in value:
        st.write(sel.get("id") +" IS A " +sel.get("type"))
