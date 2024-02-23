import streamlit as st
from snowflake.snowpark import Session
import snowflake.connector
from pandas import DataFrame

st.set_page_config(page_title="Test Webpage", page_icon=":tada:", layout="wide")
conn = st.connection("snowflake")

cur = conn.cursor()

with st.container():
    st.image("https://www.snowflake.com/wp-content/uploads/2022/03/SOLAR_Blog.png",width=600)
    st.title("Snowflake Monitor")
    st.write(
          " This app is to display information about your Snowflake database")
with st.container():
    st.header("Database Info")
    db_name=cur.execute("select current_database()").fetchone()[0]
    time = cur.execute("select current_timestamp()").fetchone()[0]
    ware = cur.execute("select current_warehouse()").fetchone()[0]
    ver = cur.execute("select current_version()").fetchone()[0]
    DB_NAME, TIME_STAMP,WAREHOUSE_NAME,VERSION = st.columns(4)
    with DB_NAME:
        st.subheader("Database Name")
        st.write(db_name)
    with TIME_STAMP:
        st.subheader("Time")
        st.write(time)
    with WAREHOUSE_NAME:
        st.subheader("Warehouse Name")
        st.write(ware)
    with VERSION:
        st.subheader("Snowflake Version")
        st.write(ver)


with st.container():
    st.subheader("Snowflake users")
    users = cur.execute("select * from snowflake.account_usage.users").fetchall()
    names = [ x[0] for x in cur.description]
    df = DataFrame(users,columns=names)
    st.dataframe(df)