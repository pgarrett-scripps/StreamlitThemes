from typing import Dict
import streamlit as st

from streamlit_themes.component import get_theme_background_color, get_theme_secondary_background_color, \
    get_theme_primary_color, get_theme_text_color, get_theme_font, _set_theme_dict, get_preset_theme
from streamlit_themes.constants import THEMES, VALID_FONTS
from streamlit_themes.theme import Theme


def _custom_theme_widget() -> Theme:
    """
    Creates a custom theme widget for user input.

    Returns:
        Dict[str, str]: The user input for the custom theme.
    """
    st.subheader("Page Colors", divider='grey')
    c1, c2, c3 = st.columns(3)
    background_color = c1.color_picker("Background 1", get_theme_background_color())
    secondary_background_color = c2.color_picker("Background 2", get_theme_secondary_background_color())
    primary_color = c3.color_picker("Primary", get_theme_primary_color())

    st.subheader("Text Options", divider='grey')
    c1, c2 = st.columns([1, 3])
    text_color = c1.color_picker("Color", get_theme_text_color())
    current_font = get_theme_font()
    if current_font is None:
        current_font = VALID_FONTS[0]
    font = c2.selectbox("Font", VALID_FONTS, index=VALID_FONTS.index(current_font))

    return Theme(
        background_color=background_color,
        secondary_background_color=secondary_background_color,
        primary_color=primary_color,
        text_color=text_color,
        font=font
    )


def custom_theme_widget(rerun: bool = True) -> None:
    """
    Displays a custom theme widget and updates the theme on user input.

    Args:
        rerun (bool): Whether to rerun the Streamlit app after updating the theme.
    """
    theme = _custom_theme_widget()
    if st.button("Update Theme", use_container_width=True):
        _set_theme_dict(theme, rerun)


def preset_theme_widget(rerun: bool = True) -> None:
    """
    Displays a widget to select a predefined theme and updates the theme on user input.

    Args:
        rerun (bool): Whether to rerun the Streamlit app after updating the theme.
    """
    st.subheader("Select a Theme", divider='grey')
    k = st.selectbox("Theme", list(THEMES.keys()))
    theme = get_preset_theme(k)
    if st.button("Select", use_container_width=True):
        _set_theme_dict(theme, rerun)
