import streamlit as st
import requests

BASE_URL = "http://localhost:5000/api"
MAP_URL = "http://localhost:5002/api"
LIGHTING_URL = "http://localhost:5001/api"
AC_URL = "http://localhost:5003/api"
SOUND_URL = "https://localhost:5004/api"

st.title("Modular Request Resolver")

if st.button("Open Mapping Interface"):
    # Construct the URL with origin and destination parameters
    map_url = MAP_URL
    # Redirect to the mapping interface
    st.markdown(f"[Go to Mapping Interface]({map_url})")

# Song Player
# Redirect URLs
st.header("Redirect URLs")
if st.button("Go to Google"):
    st.markdown("[Google](https://www.google.com)")
if st.button("Go to GitHub"):
    st.markdown("[GitHub](https://github.com)")
if st.button("Watch YouTube Video"):
    st.markdown("[Watch YouTube Video](https://youtu.be/B1Qcb5xQ96M?si=OBDkWUGTC7WQM9Je)")

# Lighting and AC Control
st.header("Lighting and AC Control")
intensity = st.slider("Lighting Intensity", 0, 100, 50)
if st.button("Set Lighting"):
    response = requests.post(f"{LIGHTING_URL}/lighting/set", json={"intensity": intensity})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))

if st.button("Get Lighting"):
    response = requests.get(f"{LIGHTING_URL}/lighting/get", json={"intensity": intensity})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))

temperature = st.slider("AC Temperature (°C)", 16, 30, 22)
if st.button("Set AC Temperature"):
    response = requests.post(f"{AC_URL}/ac/set", json={"temperature": temperature})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))

if st.button("get AC Temperature"):
    response = requests.get(f"{AC_URL}/ac/get", json={"temperature": temperature})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))

volume= st.slider("Stereo Output", 0, 100, 50)
if st.button("Set volume"):
    response = requests.post(f"{SOUND_URL}/volume/set", json={"volume": volume})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))

if st.button("Get Volume"):
    response = requests.get(f"{SOUND_URL}/volume", json={"volume": volume})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error","An error occured"))

if st.button("Mute"):
    response = requests.post(f"{SOUND_URL}/mute", json={"volume": volume})
    if response.status_code == 200:
        st.write(response.json()["result"])
    else:
        st.error(response.json().get("error", "An error occurred"))


