import streamlit as st
import json
import os
from PIL import Image

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    st.set_page_config(page_title="AI-Powered Newspaper Analysis", layout="wide")

    # Load JSON data
    json_file = "output.json"  # Ensure this file exists
    data = load_json(json_file)

    # Title and Audio Player
    st.title("📰 AI-Powered Newspaper Analysis System")

    # Audio Button
    audio_path = "Voice/speech.mp3"
    if os.path.exists(audio_path):
        st.audio(audio_path, format="audio/mp3")

    st.subheader("Latest AI-Generated News")

    # Display News Content
    st.markdown(f"<div style='font-size:18px;'>{data.get('content', 'No content available')}</div>", unsafe_allow_html=True)

    # Load and display images with descriptions
    images_folder = "cropped_images"
    for key in data:
        if key.startswith("img"):  # Checking for image keys
            img_index = key.replace("img", "")  # Extracting image number
            img_filename = f"{img_index}.png"  # Assuming images are numbered
            img_path = os.path.join(images_folder, img_filename)
            
            if os.path.exists(img_path):
                image = Image.open(img_path)
                resized_image = image.resize((400, 300))  # Smaller image size
                
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(resized_image, use_container_width=True)
                with col2:
                    st.markdown(f"<div style='font-size:16px; font-weight:bold;'>{data[key]}</div>", unsafe_allow_html=True)
            else:
                st.warning(f"Image not found: {img_path}")

if __name__ == "__main__":
    main()
