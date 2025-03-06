import streamlit as st
from PIL import Image

st.subheader("Colored image to Grayscale Converter")

upload_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    camera_img = st.camera_input("Camera")


def grayscale_img(photo):
    # Create a pillow image instance
    img = Image.open(photo)

    gray_img = img.convert("L")
    st.image(gray_img)

if camera_img:
    grayscale_img(camera_img)

if upload_image:
    grayscale_img(upload_image)




# When the user uploads an image
