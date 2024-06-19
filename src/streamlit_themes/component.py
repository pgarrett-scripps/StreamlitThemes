from typing import Optional, Dict, Union

import streamlit as st
from streamlit_themes.constants import THEMES, VALID_FONTS
from streamlit_themes.theme import Theme


def _valid_color(color: str):
    """
    Validates if the color is in the format '#RRGGBB'.

    Args:
        color (str): The color code to validate.

    Returns:
        str: The valid color code.

    Raises:
        ValueError: If the color code is not in the correct format.
    """
    if not color.startswith("#") or len(color) != 7:
        raise ValueError(f"Color: {color} must be in the format '#RRGGBB'")
    return color


def _valid_font(font: str):
    """
    Validates if the font is in the list of valid fonts.

    Args:
        font (str): The font to validate.

    Returns:
        str: The valid font.

    Raises:
        ValueError: If the font is not in the list of valid fonts.
    """
    if font not in VALID_FONTS:
        raise ValueError(f"Font: {font} must be one of {VALID_FONTS}")
    return font


def _set_theme_option(option: str, value: Optional[str], validate_func, rerun: bool):
    """
    Sets a theme option after validation and optionally reruns the Streamlit app.

    Args:
        option (str): The theme option to set.
        value (Optional[str]): The value to set for the theme option.
        validate_func (function): The validation function to apply to the value.
        rerun (bool): Whether to rerun the Streamlit app.
    """
    if value is None:
        return

    st._config._set_option(option, validate_func(value), "session")

    if rerun:
        st.rerun()


def set_theme_background_color(color: Optional[str], rerun: bool = True):
    """
    Sets the background color of the theme.

    Args:
        color (Optional[str]): The background color to set.
        rerun (bool): Whether to rerun the Streamlit app.
    """
    _set_theme_option("theme.backgroundColor", color, _valid_color, rerun)


def set_theme_primary_color(color: Optional[str], rerun: bool = True):
    """
    Sets the primary color of the theme.

    Args:
        color (Optional[str]): The primary color to set.
        rerun (bool): Whether to rerun the Streamlit app.
    """
    _set_theme_option("theme.primaryColor", color, _valid_color, rerun)


def set_theme_secondary_background_color(color: Optional[str], rerun: bool = True):
    """
    Sets the secondary background color of the theme.

    Args:
        color (Optional[str]): The secondary background color to set.
        rerun (bool): Whether to rerun the Streamlit app.
    """
    _set_theme_option("theme.secondaryBackgroundColor", color, _valid_color, rerun)


def set_theme_text_color(color: Optional[str], rerun: bool = True):
    """
    Sets the text color of the theme.

    Args:
        color (Optional[str]): The text color to set.
        rerun (bool): Whether to rerun the Streamlit app.
    """
    _set_theme_option("theme.textColor", color, _valid_color, rerun)


def set_theme_font(font: Optional[str], rerun: bool = True):
    """
    Sets the font of the theme.

    Args:
        font (Optional[str]): The font to set.
        rerun (bool): Whether to rerun the Streamlit app.
    """
    _set_theme_option("theme.font", font, _valid_font, rerun)


def _set_theme_dict(theme: Union[Dict[str, str], Theme], rerun: bool = True):
    """
    Sets all theme options with the given theme.

    Args:
        theme (Dict[str, str]): The theme options to set.
        rerun (bool): Whether to rerun the Streamlit app.
    """

    if isinstance(theme, Dict):
        theme = Theme.from_dict(theme)

    set_theme(theme.background_color, theme.primary_color, theme.secondary_background_color, theme.text_color,
              theme.font, rerun)


def set_theme(background_color: Optional[str],
              primary_color: Optional[str],
              secondary_background_color: Optional[str],
              text_color: Optional[str],
              font: Optional[str],
              rerun: bool = True):
    """
    Sets all theme options with the given values.

    Args:
        background_color (Optional[str]): The background color to set.
        primary_color (Optional[str]): The primary color to set.
        secondary_background_color (Optional[str]): The secondary background color to set.
        text_color (Optional[str]): The text color to set.
        font (Optional[str]): The font to set.
        rerun (bool): Whether to rerun the Streamlit app.

    """
    set_theme_background_color(background_color, False)
    set_theme_primary_color(primary_color, False)
    set_theme_secondary_background_color(secondary_background_color, False)
    set_theme_text_color(text_color, False)
    set_theme_font(font, False)

    if rerun:
        st.rerun()


def _get_theme_option(option: str) -> Optional[str]:
    """
    Gets the value of a theme option.

    Args:
        option (str): The theme option to get.

    Returns:
        str: The value of the theme option.

    Raises:
        ValueError: If the theme option is not set.
    """
    value = st._config.get_option(option)

    return value


def get_theme_background_color() -> Optional[str]:
    """
    Gets the background color of the theme.

    Returns:
        str: The background color of the theme.
    """
    return _get_theme_option("theme.backgroundColor")


def get_theme_primary_color() -> Optional[str]:
    """
    Gets the primary color of the theme.

    Returns:
        str: The primary color of the theme.
    """
    return _get_theme_option("theme.primaryColor")


def get_theme_secondary_background_color() -> Optional[str]:
    """
    Gets the secondary background color of the theme.

    Returns:
        str: The secondary background color of the theme.
    """
    return _get_theme_option("theme.secondaryBackgroundColor")


def get_theme_text_color() -> Optional[str]:
    """
    Gets the text color of the theme.

    Returns:
        str: The text color of the theme.
    """
    return _get_theme_option("theme.textColor")


def get_theme_font() -> Optional[str]:
    """
    Gets the font of the theme.

    Returns:
        str: The font of the theme.
    """
    return _get_theme_option("theme.font")


def get_theme() -> Theme:
    """
    Gets all theme options as a dict.

    Returns:
        Dict[str, str]: The theme options as a dictionary.
    """
    return Theme(
        background_color=get_theme_background_color(),
        primary_color=get_theme_primary_color(),
        secondary_background_color=get_theme_secondary_background_color(),
        text_color=get_theme_text_color(),
        font=get_theme_font()
    )


def get_preset_theme(key: str) -> Theme:
    """
    Chooses a theme from predefined themes.

    Args:
        key (str): The key of the theme to choose.

    Returns:
        Dict[str, str]: The theme options of the chosen theme

    Raises:
        ValueError: If the theme key is not found in the predefined themes.
    """
    if key not in THEMES:
        raise ValueError(f"Palette: {key} not found")

    theme = Theme(
        background_color=THEMES[key]['background_color'],
        primary_color=THEMES[key]['primary_color'],
        secondary_background_color=THEMES[key]['secondary_background_color'],
        text_color=THEMES[key]['text_color'],
        font=THEMES[key]['font']
    )

    return theme


def set_preset_theme(key: str, rerun: bool = False) -> None:
    """
    Updates the theme with a predefined theme.

    Args:
        key (str): The key of the theme to choose.
        rerun (bool): Whether to rerun the Streamlit app.

    Returns:
        Dict[str, str]: The theme options of the chosen theme

    Raises:
        ValueError: If the theme key is not found in the predefined themes.

    """
    theme = get_preset_theme(key)
    _set_theme_dict(theme, rerun)


def generate_theme_config_string(theme: Optional[Union[Dict[str, str], Theme]] = None) -> str:
    """
    Generates a theme configuration string in the specified format. If no theme is provided, the current theme is used.

    Returns:
        str: The theme configuration string.
    """

    if theme is None:
        theme = get_theme()

    if isinstance(theme, Dict):
        theme = Theme.from_dict(theme)

    return theme.to_streamlit_config_string()


def parse_theme_config_string(config_string: str) -> Theme:
    """
    Parses a theme configuration string into a dictionary.

    Args:
        config_string (str): The theme configuration string to parse.

    Returns:
        Dict[str, str]: The theme configuration as a dictionary.
    """
    return Theme.from_config_string(config_string)


def get_all_preset_themes() -> Dict[str, Theme]:
    """
    Gets all predefined themes.

    Returns:
        Dict[str, Dict[str, str]]: The predefined themes.
    """
    return {k: get_preset_theme(k) for k in THEMES.keys()}
