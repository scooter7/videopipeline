import streamlit as st
import flickrapi
import requests
from PIL import Image
import numpy as np
from moviepy.editor import concatenate_videoclips, AudioFileClip, CompositeAudioClip, ImageClip
import tempfile
from moviepy.video.fx.all import fadein, fadeout
import pandas as pd
import cv2
import numpy as np
import tempfile
import os
from moviepy.editor import AudioFileClip, VideoFileClip

# Placeholder function definitions for the content of each file.
# Replace the content of these functions with the actual content of your Python files.

def pv_code():
    """
    # Initialize session state variables if they don't exist
if 'processing_done' not in st.session_state:
    st.session_state.processing_done = False

video_file = st.file_uploader("Choose a video file", type=["mp4"])
csv_file = st.file_uploader("Choose a CSV file")

# Button to start processing
start_processing = st.button('Start Processing')

if start_processing:
    st.session_state.processing_done = False  # Reset the flag when button is pressed

if video_file and csv_file and not st.session_state.processing_done:
    df = pd.read_csv(csv_file)
    first_names = df['FirstName'].tolist()

    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
        tmp.write(video_file.getvalue())
        video_path = tmp.name

    original_clip = VideoFileClip(video_path)
    audio = original_clip.audio

    for name in first_names:
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        temp_video_path = tempfile.mktemp(suffix='.mp4')
        out = cv2.VideoWriter(temp_video_path, fourcc, fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            font = cv2.FONT_HERSHEY_SIMPLEX
            text = f"{name}, please enroll at ABC College"
            text_position = (50, height - 50)
            font_scale = 1
            font_color = (255, 255, 255)
            line_type = 2

            cv2.putText(frame, text, text_position, font, font_scale, font_color, line_type)
            out.write(frame)

        cap.release()
        out.release()

        processed_clip = VideoFileClip(temp_video_path)
        final_clip = processed_clip.set_audio(audio)
        final_output_filename = f"personalized_{name}.mp4"
        final_clip.write_videofile(final_output_filename, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)

        with open(final_output_filename, "rb") as file:
            st.download_button(f"Download {name}'s Video", file, file_name=final_output_filename, mime="video/mp4")

        os.remove(temp_video_path)
        os.remove(final_output_filename)

    os.unlink(video_path)
    st.session_state.processing_done = True  # Set flag to True after processing
    """
    code = """
# Paste pv.py content here, keeping the triple quotes.
"""
    return code

def imagetovideo_code():
    """
    def resize_and_pad(img, size, pad_color=(255, 255, 255)):
    img.thumbnail(size, Image.Resampling.LANCZOS)
    background = Image.new('RGB', size, pad_color)
    img_w, img_h = img.size
    bg_w, bg_h = size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    return np.array(background)

def generate_video_from_images(image_files, size=(640, 480), duration_per_image=3, fade_duration=1):
    clips = []
    for img_file in image_files:
        img = resize_and_pad(Image.open(img_file), size)
        clip = ImageClip(np.array(img)).set_duration(duration_per_image)
        if fade_duration > 0:
            clip = fadein(clip, fade_duration)
            clip = fadeout(clip, fade_duration)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    return video

def add_audio_to_video(video_clip, speech_audio=None, background_audio=None):
    if speech_audio:
        speech_audio.seek(0)
        speech_clip = AudioFileClip(speech_audio.name).set_duration(video_clip.duration)
    else:
        speech_clip = None

    if background_audio:
        background_audio.seek(0)
        background_clip = AudioFileClip(background_audio.name).volumex(0.1).set_duration(video_clip.duration)
    else:
        background_clip = None

    if speech_clip or background_clip:
        final_audio = CompositeAudioClip([clip for clip in [speech_clip, background_clip] if clip is not None])
        video_clip = video_clip.set_audio(final_audio)
    return video_clip

st.title('Video Generator App')

uploaded_images = st.file_uploader("Upload Images", accept_multiple_files=True, type=['jpg', 'jpeg', 'png'])
image_display_duration = st.slider("Select how many seconds to display each image:", min_value=1, max_value=10, value=3)
add_fades = st.checkbox("Add fade transitions between images", value=True)
fade_duration = 1 if add_fades else 0

uploaded_speech = st.file_uploader("Upload Speech Audio (MP3)", type=['mp3'], accept_multiple_files=False)
uploaded_background = st.file_uploader("Upload Background Audio (MP3)", type=['mp3'], accept_multiple_files=False)

if st.button('Generate Video') and uploaded_images:
    speech_temp = tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") if uploaded_speech else None
    background_temp = tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") if uploaded_background else None

    if speech_temp:
        speech_temp.write(uploaded_speech.getvalue())
        speech_temp.seek(0)
    if background_temp:
        background_temp.write(uploaded_background.getvalue())
        background_temp.seek(0)

    video_clip = generate_video_from_images(uploaded_images, duration_per_image=image_display_duration, fade_duration=fade_duration if add_fades else 0)
    video_clip = add_audio_to_video(video_clip, speech_temp, background_temp)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as final_video_file:
        video_clip.write_videofile(final_video_file.name, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True, fps=24)
        st.video(final_video_file.name)
        final_video_file.seek(0)
        st.download_button(label="Download Video", data=final_video_file.read(), file_name="final_video.mp4", mime="video/mp4")
else:
    st.error("Please upload the required images.")
    """
    code = """
# Paste imagetovideo.py content here, keeping the triple quotes.
"""
    return code

def images_code():
    """
    FLICKR_PUBLIC = st.secrets["flickr"]["api_key"]
FLICKR_SECRET = st.secrets["flickr"]["api_secret"]
flickr = flickrapi.FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')

def fetch_flickr_images(search_term):
    photos = flickr.photos.search(text=search_term, per_page=100, media='photos')  # Fetching 100 images
    urls = []
    for photo in photos['photos']['photo']:
        url = f"https://live.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}_w.jpg"
        urls.append(url)
    return urls

def fetch_wikimedia_images(search_term):
    SEARCH_URL = "https://commons.wikimedia.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'generator': 'search',
        'gsrnamespace': 6,
        'gsrsearch': search_term,
        'gsrlimit': 5,
        'prop': 'imageinfo',
        'iiprop': 'url',
        'iiurlwidth': 200,
    }
    response = requests.get(SEARCH_URL, params=params).json()
    images = []
    if 'query' in response:
        for page_id in response['query']['pages']:
            image_info = response['query']['pages'][page_id]['imageinfo'][0]
            images.append(image_info['url'])
    return images

st.title("Image Search App")
search_term = st.text_input("Enter a search term:")

if search_term:
    flickr_images = fetch_flickr_images(search_term)
    wikimedia_images = fetch_wikimedia_images(search_term)
    
    if flickr_images:
        st.subheader("Flickr Images:")
        for image_url in flickr_images:
            st.image(image_url, use_column_width=True)
    else:
        st.write("No Flickr images found.")
        
    if wikimedia_images:
        st.subheader("Wikimedia Commons Images:")
        for image_url in wikimedia_images:
            st.image(image_url, use_column_width=True)
    else:
        st.write("No Wikimedia Commons images found.")
else:
    st.write("Please enter a search term.")
    """
    code = """
# Paste images.py content here, keeping the triple quotes.
"""
    return code

# Create Streamlit tabs
tab1, tab2, tab3 = st.tabs(["PV", "ImageToVideo", "Images"])

with tab1:
    st.code(pv_code(), language='python')

with tab2:
    st.code(imagetovideo_code(), language='python')

with tab3:
    st.code(images_code(), language='python')
