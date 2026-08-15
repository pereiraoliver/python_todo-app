# Import streamlit for building the web app and PIL for image processing
import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Display a camera input widget and capture the image from the user
    camera_image = st.camera_input("Camera")

# Open the captured image using PIL (Python Imaging Library)
if camera_image:
    img = Image.open(camera_image)

    # Convert the image to grayscale (mode "L" = 8-bit pixels, black and white)
    gray_image = img.convert("CMYK")

    # Display the grayscale image in the Streamlit app
    st.image(gray_image)

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_image = img.convert("L")
    st.image(gray_image)
