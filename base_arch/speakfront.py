import streamlit as st
import requests
from flask import jsonify

st.title("Stereo Module Controller")

volume= st.slider("Stereo Output", 0, 100, 50)
if st.button("Set volume"):
    response = requests.post(f"http://127.0.0.1:5010/volume/set", json={"volume": volume})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))

if st.button("Get Volume"):
    response = requests.get(f"http://127.0.0.1:5010/volume/get", json={"volume": volume})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error","An error occured"))

if st.button("Mute"):
    response = requests.post(f"http://127.0.0.1:5010/volume/mute", json={"volume": volume})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))

if st.button("Unmute"):
    response = requests.post(f"http://127.0.0.1:5010/volume/unmute", json={"volume": volume})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))