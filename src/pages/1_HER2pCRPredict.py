import os
from joblib import load

import streamlit as st
from streamlit_helpers.sidebar_logo import add_logo

if "logo_path" in st.session_state:
    logo_path = st.session_state["logo_path"]
    add_logo(logo_path)


# st.markdown(
#     """###  <div style="text-align: left"> HER2pCRPredict </div>""",
#     unsafe_allow_html=True,
# )
# st.text("")

st.markdown(
    """###  <div style="text-align: left"> Predictors of pathological complete response </div>""",
    unsafe_allow_html=True,
)
st.text("")
st.info(
    """
HER2pCRPredict is an advanced online calculator designed to assist clinicians in predicting the likelihood of a pathologic complete response (pCR) following neoadjuvant treatment with chemotherapy (with or without anthracyclines), trastuzumab, and pertuzumab in patients with HER2-positive breast cancer. By leveraging the latest research and clinical data, this tool offers a user-friendly interface to guide treatment decisions and enhance patient outcomes.
Our goal is to support your clinical judgment by providing a reliable resource for managing HER2+ breast cancer, ultimately leading to more precise and effective treatment strategies.

Explore HER2pCRPredict today and take a step towards optimized cancer care.
"""
)

st.text("")

with st.expander("Calculator", expanded=True):
    st.markdown(
        """ <div style="font-style: Justify"> <div style="font-style: italic"> Complete with clinical and pathological characteristics at diagnosis. <div/>"""
    , unsafe_allow_html=True)
    st.text("")


    value_age_diagnosis = st.number_input(
        "**Age at diagnosis**",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )
    value_tumor_size = st.number_input(
        "**Tumor size**",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )


    value_nodal_disease = st.number_input(
        "**Nodal staging**",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )


    value_strogen_perc = st.number_input(
        "**Estrogen receptor expression %**",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )

    value_progest_perc = st.number_input(
        "**Progesteron  receptor expression %**",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )

    value_grade = st.number_input(
        "**Grade**",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )

    value_ki67 = st.number_input(
        "**Ki67 %**",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )
    
    model = load(
        open(os.path.join(os.getcwd(), "src/models/paulo/model_20240829.pkl"), "rb")
    )

    input_values = [value_age_diagnosis, value_tumor_size, value_nodal_disease, value_strogen_perc, value_progest_perc, value_grade, value_ki67]

if st.button("Start"):
    if any([True for i in input_values if i == 0]):
        st.warning(
            """Warning: One or more values are **zero**.
            This is allowed, but make sure to check it is valid."""
        )

    st.markdown("")
    st.markdown(
        f"""The probability of **pCR** is:
    <br/>
    <font size="6"> {model.predict_proba([input_values])[0][0]*100:.2f}% </font>""",
        unsafe_allow_html=True,
    )