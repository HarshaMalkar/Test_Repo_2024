import pandas as pd
import json
import streamlit as st
import time
from snowflake.snowpark import Session

st.title('❄️ How to connect Streamlit to a Snowflake database')

# Establish Snowflake session
@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets.connections.snowflake).create()

session = create_session()
st.success("Connected to Snowflake!")

# Load data table
@st.cache_data
def load_data(table_name):
    ## Read in data table
    st.write(f"Here's some example data from `{table_name}`:")
    table = session.table(table_name)
    
    ## Do some computation on it
    table = table.limit(100)
    
    ## Collect the results. This will run the query and download the data
    table = table.collect()
    return table

# Select and display data table
table_name = "SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.customer"

## Display data table
with st.expander("See Table"):
    df = load_data(table_name)
    st.dataframe(df)

with st.form("data_editor_form"):
    st.caption("Edit the dataframe below")
    edited = st.data_editor(df, use_container_width=True, num_rows="dynamic")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    try:
        #Note the quote_identifiers argument for case insensitivity
        session.write_pandas(edited, "SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.customer", overwrite=True, quote_identifiers=False)
        st.success("Table updated")
        time.sleep(500)
    except:
        st.warning("Error updating table")
    #display success message for 5 seconds and update the table to reflect what is in Snowflake
    st.experimental_rerun()    