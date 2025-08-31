import streamlit as st
from PIL import Image
import base64
from io import BytesIO


class StyleManager:

    def __init__(self, img_path):
        self.img_path = img_path


    def _image_to_base64(self):
        img = Image.open(self.img_path)

        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()


    def display_header(self, title):
        logo = self._image_to_base64()

        col1, col2 = st.columns([1, 2])

        col1.markdown(
            f"""
            <div style="display: flex; justify-content: left; align-items: left; margin-top: -30px">
                <img src="data:image/png;base64,{logo}" width="150"/>
            </div>
            """, unsafe_allow_html=True
        )

        col2.title(title, anchor=False)

        st.subheader("")