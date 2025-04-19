import streamlit as st
import pandas as pd
import sqlite3
from slot_manager import get_available_slots

st.title("🚗 Smart Parking Dashboard")
conn = sqlite3.connect("parking.db")
df = pd.read_sql("SELECT * FROM parking_events ORDER BY timestamp DESC", conn)
conn.close()

st.metric("🅿️ Available Slots", get_available_slots())
st.dataframe(df)
