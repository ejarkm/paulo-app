import os
from joblib import load

import streamlit as st


st.markdown(
    """###  <div style="text-align: left"> Paulo Predictors </div>""",
    unsafe_allow_html=True,
)
st.text("")
st.info(
    """
More text to complete
"""
)

st.text("")

with st.expander("Calculator", expanded=True):
    st.markdown(
        """ <div style="font-style: Justify"> <div style="font-style: italic"> To complete <div/>"""
    , unsafe_allow_html=True)
    st.text("")

    value_das = st.number_input(
        "**..",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )
    value_pcr = st.number_input(
        "**......",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )
    value_ril6il2 = st.number_input(
        "**....",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )

    value_4 = st.number_input(
        "**4",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )
    value_5 = st.number_input(
        "**5",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )
    value_6 = st.number_input(
        "**6",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )
    value_7 = st.number_input(
        "**7",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
    )

    # Del modelo, el label 1 es ser RESPONDEDOR, que en las posiciones de las predicciones es la 0
    respondedor = 1
    # Del modelo, el label 2 es ser NO RESPONDEDOR, que en las posiciones de las predicciones es la 1
    no_respondedor = 2

    model = load(
        open(os.path.join(os.getcwd(), "models/paulo/model_20240810.pkl"), "rb")
    )

    input_values = [value_das, value_pcr, value_ril6il2,value_4,value_5,value_6,value_7]

if st.button("Start"):
    if any([True for i in input_values if i == 0]):
        st.warning(
            """Warning: One or more values are **zero**.
            This is allowed, but make sure to check it is valid."""
        )

    st.markdown("")
    st.markdown(
        f"""The probability of being ... is:
    <br/>
    <font size="6"> {model.predict_proba([input_values])[0][0]*100:.2f}% </font>""",
        unsafe_allow_html=True,
    )