import streamlit as st
import base64


def _get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def add_logo(logo_path):
    logo_bin = _get_base64_of_bin_file(logo_path)
    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url("data:{logo_path};base64,{logo_bin}");
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: center;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )