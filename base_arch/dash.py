import streamlit as st
from queue import PriorityQueue
import os
from pygame import mixer  # We'll use pygame to handle audio playback

# Initialize the pygame mixer
mixer.init()

''' Define file paths for the uploaded songs
song1_path = r'#add file path from the folder'
song2_path = r'#add file path from the folder'''

request_queue = PriorityQueue()

def handle_request(request_type, value):
    # Define priorities
    priorities = {
        "Music": 3,
        "Maps": 1,
        "Lighting": 2,
        "Air Conditioning": 2
    }
    priority = priorities[request_type]
    request_queue.put((priority, request_type, value))
    process_requests()

def process_requests():
    if not request_queue.empty():
        priority, request_type, value = request_queue.get()
        if request_type == "Music":
            if value == "Stop":
                mixer.music.stop()
                st.success("Music stopped")
            else:
                mixer.music.load(value)
                mixer.music.play()
                st.success(f"Playing {os.path.basename(value)}")
        if request_type == "Maps":
            start, end = value
            st.success(f"Navigating from {start} to {end}")
        elif request_type == "Lighting":
            brightness, color = value
            st.session_state.brightness = brightness
            st.session_state.color = color
            st.success(f"Lighting set to {brightness}% and color {color}")
        elif request_type == "Air Conditioning":
            st.success(f"Temperature set to {value}°C")

def car_dashboard():
    st.title("Dashboard of a Car")
    st.header("Car Control Panel")
    
    # Initialize session state for lighting
    if 'brightness' not in st.session_state:
        st.session_state.brightness = 50
    if 'color' not in st.session_state:
        st.session_state.color = '#ffff00'  # Default color: yellow
    
    # Create containers for each section
    music_container = st.container()
    maps_container = st.container()
    lighting_container = st.container()
    ac_container = st.container()
    
    # Music Section
    with music_container:
        st.subheader("Music")
                # Initialize session state variables if they don't exist
    if 'playlist' not in st.session_state:
        st.session_state.playlist = []
    if 'current_song' not in st.session_state:
        st.session_state.current_song = None
    if 'current_song_name' not in st.session_state:
        st.session_state.current_song_name = None
    if 'is_playing' not in st.session_state:
        st.session_state.is_playing = False

    # File uploader for multiple audio files
    uploaded_files = st.file_uploader("Choose audio files", type=['mp3', 'wav', 'ogg'], accept_multiple_files=True)

    # Predefined file paths
    song1_path = r'/Users/shreya/Downloads/Death Grips - Get Got.mp3'
    song2_path = r'/Users/shreya/Downloads/Death Grips - The Fever (Aye Aye).mp3'

    # Add predefined songs to the playlist
    predefined_songs = [song1_path, song2_path]
    for song_path in predefined_songs:
        with open(song_path, 'rb') as f:
            file_bytes = f.read()
            if (os.path.basename(song_path), file_bytes) not in st.session_state.playlist:
                st.session_state.playlist.append((os.path.basename(song_path), file_bytes))

    # Add uploaded files to the playlist
    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_bytes = uploaded_file.read()
            if (uploaded_file.name, file_bytes) not in st.session_state.playlist:
                st.session_state.playlist.append((uploaded_file.name, file_bytes))

    # Display the playlist
    st.write("Playlist:")
    for i, (filename, _) in enumerate(st.session_state.playlist):
        st.write(f"Track {i+1}: {filename}")

    # Dropdown to select a song to play
    song_to_play = st.selectbox("Choose a song to play:", [filename for filename, _ in st.session_state.playlist])

    # Play the selected song
    if st.button("Start"):
        for filename, file_bytes in st.session_state.playlist:
            if filename == song_to_play:
                st.session_state.current_song = file_bytes
                st.session_state.current_song_name = filename
                st.session_state.is_playing = True
                break

    # Stop the currently playing song
    if st.button("Stop"):
        st.session_state.is_playing = False
        st.session_state.current_song = None
        st.session_state.current_song_name = None

    # If a song is playing, display the audio player and the "Now playing" message
    if st.session_state.is_playing and st.session_state.current_song:
        st.audio(st.session_state.current_song, format='audio/mp3', start_time=0)
        st.write(f"Now playing: {st.session_state.current_song_name}")

    
    # Maps Section
    with maps_container:
        st.subheader("Maps")
        start_point = st.text_input("Enter Start Point:")
        end_point = st.text_input("Enter End Point:")
        if st.button("Navigate"):
            handle_request("Maps", (start_point, end_point))
    
    # Lighting Section
    with lighting_container:
        st.subheader("Lighting")
        light_level = st.slider("Adjust Lighting Level:", 0, 100, 50)
        light_color = st.color_picker("Pick a light color:", '#ffff00')  # Default color: yellow
        if st.button("Set Lighting"):
            handle_request("Lighting", (light_level, light_color))
        # Display light fixture brightness and color
        st.text("Light Fixture:")
        st.markdown(
            f"<div style='width: 100%; height: 50px; background-color: {st.session_state.color}; opacity: {st.session_state.brightness / 100};'></div>",
            unsafe_allow_html=True
        )
    
    # Air Conditioning Section
    with ac_container:
        st.subheader("Air Conditioning")
        ac_temp = st.slider("Set Temperature:", 16, 30, 22)
        if st.button("Set Temperature"):
            handle_request("Air Conditioning", ac_temp)

if __name__ == "__main__":
    car_dashboard()