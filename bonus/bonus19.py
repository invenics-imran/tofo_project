import streamlit as st
from PIL import Image

with st.expander("open camera"):
    # start camera
    camera_image=st.camera_input("camera")

print(camera_image)

if camera_image:
    # create a PIL image instance
    img=Image.open(camera_image)

    # convert the pillow image to grayscale "L" is a notation
    gray_img=img.convert("L")

    # rander the grays scale image to webpage
    st.image(gray_img)
     