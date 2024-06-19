from typing import Optional, Tuple

import streamlit as st
from stthemes.constants import THEMES, VALID_FONTS


def _valid_color(color: str):
    if not color.startswith("#") or len(color) != 7:
        raise ValueError(f"Color: {color} must be in the format '#RRGGBB'")
    return color


def _valid_font(font: str):
    if font not in VALID_FONTS:
        raise ValueError(f"Font: {font} must be one of {VALID_FONTS}")
    return font


def set_theme_background_color(color: Optional[str], rerun: bool = False):
    if color is None:
        return

    st._config._set_option("theme.backgroundColor", _valid_color(color), "session")

    if rerun:
        st.rerun()


def set_theme_primary_color(color: Optional[str], rerun: bool = False):
    if color is None:
        return

    st._config._set_option("theme.primaryColor", _valid_color(color), "session")

    if rerun:
        st.rerun()


def set_theme_secondary_background_color(color: Optional[str], rerun: bool = False):
    if color is None:
        return

    st._config._set_option("theme.secondaryBackgroundColor", _valid_color(color), "session")

    if rerun:
        st.rerun()


def set_theme_text_color(color: Optional[str], rerun: bool = False):
    if color is None:
        return

    st._config._set_option("theme.textColor", _valid_color(color), "session")

    if rerun:
        st.rerun()


def set_theme_font(font: Optional[str], rerun: bool = False):
    if font is None:
        return

    st._config._set_option("theme.font", _valid_font(font), "session")

    if rerun:
        st.rerun()


def get_theme_background_color() -> str:
    color = st._config.get_option("theme.backgroundColor")

    if color is None:
        raise ValueError("Theme background color not set. Likely a custom theme has not been set in .streamlit/config.toml")

    return color


def get_theme_primary_color() -> str:
    color= st._config.get_option("theme.primaryColor")

    if color is None:
        raise ValueError(
            "Theme background color not set. Likely a custom theme has not been set in .streamlit/config.toml")

    return color


def get_theme_secondary_background_color() -> str:
    color= st._config.get_option("theme.secondaryBackgroundColor")

    if color is None:
        raise ValueError(
            "Theme background color not set. Likely a custom theme has not been set in .streamlit/config.toml")

    return color


def get_theme_text_color() -> str:
    color=  st._config.get_option("theme.textColor")

    if color is None:
        raise ValueError(
            "Theme background color not set. Likely a custom theme has not been set in .streamlit/config.toml")

    return color


def get_theme_font() -> str:
    font = st._config.get_option("theme.font")

    if font is None:
        raise ValueError(
            "Theme font not set. Likely a custom theme has not been set in .streamlit/config.toml")

    return font


def get_theme() -> Tuple[str, str, str, str, str]:
    return (get_theme_background_color(), get_theme_primary_color(), get_theme_secondary_background_color(),
            get_theme_text_color(), get_theme_font())


def update_theme(background_color: Optional[str] = None,
                 primary_color: Optional[str] = None,
                 secondary_background_color: Optional[str] = None,
                 text_color: Optional[str] = None,
                 font: Optional[str] = None,
                 rerun: bool = False) -> None:

    set_theme_background_color(background_color, False)
    set_theme_primary_color(primary_color, False)
    set_theme_secondary_background_color(secondary_background_color, False)
    set_theme_text_color(text_color, False)
    set_theme_font(font, False)

    if rerun:
        st.rerun()


def _custom_theme_widget() -> Tuple[str, str, str, str, str]:

    st.subheader("Page Colors", divider='grey')
    c1,c2,c3 = st.columns(3)
    background_color = c1.color_picker("Background 1", get_theme_background_color())
    secondary_background_color = c2.color_picker("Background 2", get_theme_secondary_background_color())
    primary_color = c3.color_picker("Primary", get_theme_primary_color())

    st.subheader("Text Options", divider='grey')
    c1, c2 = st.columns([1,3])
    text_color = c1.color_picker("Color", get_theme_text_color())
    font = c2.selectbox("Font", VALID_FONTS, index=VALID_FONTS.index(get_theme_font()))
    return background_color, primary_color, secondary_background_color, text_color, font


def custom_theme_widget(rerun: bool = True) -> None:
    background, primary, secondary, text, font = _custom_theme_widget()
    if st.button("Update Theme", use_container_width=True):
        update_theme(background, primary, secondary, text, font, rerun)


def chose_theme(key: str) -> Tuple[str, str, str, str, str]:
    if key not in THEMES:
        raise ValueError(f"Palette: {key} not found")

    background = THEMES[key]['backgroundColor']
    primary = THEMES[key]['primaryColor']
    secondary = THEMES[key]['secondaryBackgroundColor']
    text = THEMES[key]['textColor']

    return background, primary, secondary, text, get_theme_font()


def theme_widget(rerun: bool = True) -> None:

    st.subheader("Select a Theme", divider='grey')
    k = st.selectbox("Palette", list(THEMES.keys()))
    background, primary, secondary, text, font = chose_theme(k)
    if st.button("Select", use_container_width=True):
        update_theme(background, primary, secondary, text, font, rerun)
