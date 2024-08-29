import streamlit as st
from PIL import Image
import os
from streamlit_helpers.sidebar_logo import add_logo


execution_path = os.path.dirname(__file__)
logo_path = os.path.join(execution_path, "images", "spaik_logo.png")
favicon_path = os.path.join(execution_path, "images", "spaik_black_logo.png")
icon_path = os.path.join(execution_path, "images", "spaik_black_logo.png")


favicon = Image.open(favicon_path)
pages = st.source_util.get_pages(__file__)

main_page_name = "app"
main_page_rename = "About Spaik"
new_page_names = {
    main_page_name: main_page_rename,
    "PCR": "PCR Calculator",
}


for key, page in pages.items():
    if page["page_name"] == main_page_rename:
        pages[key]["icon"] = "📄"
    else:
        page["icon"] = "📈"
    if page["page_name"] in new_page_names:
        page["page_name"] = new_page_names[page["page_name"]]


st.set_page_config(
    page_title="Spaik-HER2Predict",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=favicon,
)

st.session_state["logo_path"] = logo_path
add_logo(logo_path=logo_path)


st.text("")
st.markdown("""### Empowering Healthcare Innovation with Artificial Intelligence""")
st.text("")



col1, col2, col3 = st.columns(3)
with col2:
    st.image(logo_path, width=200)
    

st.text("")
st.text("")
st.info(
    """
At Spaik, we believe that artificial intelligence can be used to improve patient outcomes
and reduce the cost of healthcare.
Our mission is to bring the power of AI to healthcare,
enabling healthcare providers to make better decisions faster.

For more information, please visit our website: [spaik.es](https://spaik.es)
""")


