import streamlit as st
from datetime import timedelta


def add_time():
    initial_date = st.session_state["start_date"]
    duration = int(st.session_state["days"].split(" ")[0])
    st.session_state["end_date"] = initial_date + timedelta(days=duration)
    
    
def abstract_time():
    end_date = st.session_state["end_date"]
    duration = int(st.session_state["days"].split(" ")[0])
    st.session_state["start_date"] = end_date - timedelta(days=duration)


st.radio("Select Duration",
         ["7 Days", "15 Days" , "10 Days"],
         horizontal=True,
         index=0,
         key="days",
         on_change=add_time
        )

col1 , col2 = st.columns(2)
col1.date_input("Start Date", key="start_date",on_change=add_time)
col2.date_input("End Date",key="end_date",on_change=abstract_time)


