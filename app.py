import streamlit as st
import yt_dlp
from datetime import datetime
import os

st.title("Video Downloader 🎥")

# Input box for any URL
video_url = st.text_input("Paste Link Here:", placeholder="https://www.facebook.com/...")

if st.button("Download"):
    if video_url:
        try:
            # Generate the timestamp filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"video_{timestamp}.mp4"

            # Simplified settings to avoid the FFmpeg error
            ydl_opts = {
                'format': 'best[ext=mp4]/best', # Downloads a single file with audio + video
                'outtmpl': filename,
            }

            with st.spinner("Downloading..."):
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
            
            # Show the video and the save button
            with open(filename, "rb") as file:
                st.video(file)
                st.download_button(
                    label="Save to Device",
                    data=file,
                    file_name=filename,
                    mime="video/mp4"
                )
            
            # Clean up the server file
            os.remove(filename)
            st.success("Done!")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please paste a link first.")
