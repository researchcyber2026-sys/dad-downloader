import streamlit as st
import yt_dlp
from datetime import datetime
import os

st.title("Video Downloader 🎥")

video_url = st.text_input("Paste Link Here:", placeholder="https://www.instagram.com/reel/...")

if st.button("Download"):
    if video_url:
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"video_{timestamp}.mp4"
            
            status = st.empty()
            status.info("Bypassing security... please wait.")

            # Advanced options to mimic a real browser without cookies
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': filename,
                'quiet': True,
                'no_warnings': True,
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                'add_header': [
                    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language: en-US,en;q=0.5',
                    'Referer: https://www.google.com/',
                    'DNT: 1',
                ],
                'extractor_args': {
                    'instagram': {
                        'get_test_report': [True],
                    }
                },
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            
            if os.path.exists(filename):
                with open(filename, "rb") as file:
                    status.empty()
                    st.success("Download Ready!")
                    st.download_button(
                        label="⬇️ Save to Device",
                        data=file,
                        file_name=filename,
                        mime="video/mp4"
                    )
                os.remove(filename)

        except Exception as e:
            st.error(f"Instagram Blocked the Request: {e}")
            st.info("Tip: If this fails, the Streamlit Server IP is likely temporary blacklisted. Try again in 10 minutes.")
    else:
        st.warning("Please paste a link first.")
