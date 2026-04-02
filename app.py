import streamlit as st
import yt_dlp
from datetime import datetime
import os

st.title("Video Downloader 🎥")

# Input box for the URL
video_url = st.text_input("Paste Link Here:", placeholder="https://www.facebook.com/...")

if st.button("Download"):
    if video_url:
        try:
            # Generate the timestamp filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"video_{timestamp}.mp4"

            # Status message for the user
            status = st.empty()
            status.info("Processing... please wait.")

            # Settings to grab a single MP4 file (no FFmpeg needed)
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': filename,
                'quiet': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            
            # Read the file and trigger immediate download
            if os.path.exists(filename):
                with open(filename, "rb") as file:
                    status.empty()
                    st.download_button(
                        label="✅ Click here if download didn't start",
                        data=file,
                        file_name=filename,
                        mime="video/mp4"
                    )
                    # This line below is a "hack" to try and auto-click the download for some browsers
                    st.success(f"Video {filename} is ready!")
                
                # Clean up server storage
                os.remove(filename)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please paste a link first.")
