import streamlit as st
import yt_dlp
from datetime import datetime
import os

st.set_page_config(page_title="Video Downloader", page_icon="🎥")
st.title("Dad's Video Downloader 🎥")

video_url = st.text_input("Enter Video URL:", placeholder="https://www.facebook.com/...")

if st.button("Prepare Download"):
    if video_url:
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"video_{timestamp}.mp4"
            with st.spinner("Downloading..."):
                ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', 'outtmpl': filename}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
            with open(filename, "rb") as file:
                st.video(file)
                st.download_button(label="🚀 Save Video", data=file, file_name=filename, mime="video/mp4")
            os.remove(filename)
        except Exception as e:
            st.error(f"Error: {e}")
