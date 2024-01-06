import streamlit as st
import ffmpeg

# URL RTMP server
rtmp_url = 'rtmp://example.com/live/stream_key'  # Ganti dengan URL RTMP server yang sesuai

# Halaman utama Streamlit
def main():
    st.title("Live Streaming with Streamlit and FFmpeg-Python")

    # Form input untuk URL RTMP dan URL video
    rtmp_url_input = st.text_input("Enter the RTMP URL:", rtmp_url)
    video_url = st.text_input("Enter the URL of the video:", "")

    # Tombol untuk memulai live streaming
    if st.button("Start Live Streaming"):
        if rtmp_url_input and video_url:
            st.info(f"Live streaming started to {rtmp_url_input}")
            st.warning("Please make sure FFmpeg is installed on your system.")
            start_live_stream(rtmp_url_input, video_url)
        else:
            st.error("Please provide the RTMP URL and video URL.")

# Fungsi untuk memulai live streaming
def start_live_stream(rtmp_url, video_url):
    # Command FFmpeg untuk live streaming dari URL video ke RTMP server
    ffmpeg.input(video_url).output(rtmp_url, format='flv').run(overwrite_output=True)

# Panggil fungsi utama
if __name__ == "__main__":
    main()
