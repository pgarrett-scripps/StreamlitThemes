
import streamlit as st

from streamlit_themes.component import generate_theme_config_string
from streamlit_themes.widgets import custom_theme_widget

st.title("Hello World")

st.write(
    """
    Lorem ipsum dolor sit amet,
    consectetur adipiscing elit. Sed in finibus quam. Nam elementum quam volutpat,
    aliquam enim vulputate,
    vulputate felis. Aliquam faucibus magna nibh,
    at posuere ligula suscipit sit amet. Sed purus velit,
    placerat vel dapibus a,
    posuere ut dui. Orci varius natoque penatibus et magnis dis parturient montes,
    """
)

st.slider("Slider", 0, 100, 50)

st.number_input("Number Input", 0, 100, 50)

st.text_input("Text Input", "Hello World")

c1, c2 = st.columns(2)
c1.button("Button", use_container_width=True)
c2.button("Button", type="primary", use_container_width=True)

with st.sidebar:
    st.header("Custom Theme")
    custom_theme_widget()

    st.header("Theme Configuration", divider="grey")
    st.caption("Copy this and add it to your apps .streamlit/config.toml file.")
    st.code(generate_theme_config_string())