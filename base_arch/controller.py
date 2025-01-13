# streamlit_app.py
import streamlit as st
import requests

st.title("Master Control Interface")

# Lighting Control Section
st.header("Lighting Control")
lighting_setting = st.text_input("Set Lighting")
if st.button("Set Lighting"):
    response = requests.post("http://localhost:5001/api/lighting/set", json={"setting": lighting_setting})
    if response.status_code == 200:
        st.success("Lighting setting updated successfully!")
    else:
        st.error("Failed to update lighting setting")

if st.button("Get Lighting"):
    response = requests.get("http://localhost:5001/api/lighting/get")
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("Failed to get lighting setting")

# Mapping Directions Section
st.header("Mapping Directions")
origin = st.text_input("Origin")
destination = st.text_input("Destination")
if st.button("Get Directions"):
    response = requests.get(f"http://localhost:5002/api/mapping/directions?origin={origin}&destination={destination}")
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("Failed to get directions")
