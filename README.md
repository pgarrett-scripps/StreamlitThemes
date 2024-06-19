# Streamlit Theme Manager

This project is a Streamlit Theme Manager that allows users to dynamically update the theme of their Streamlit app. It provides functions to set and get theme colors and fonts, as well as widgets to customize and select predefined themes.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/streamlit-theme-manager.git
    ```

2. Navigate to the project directory:
    ```bash
    cd streamlit-theme-manager
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Setting Theme Colors and Fonts

You can set various theme attributes using the provided functions:

- `set_theme_background_color(color: Optional[str], rerun: bool = False)`
- `set_theme_primary_color(color: Optional[str], rerun: bool = False)`
- `set_theme_secondary_background_color(color: Optional[str], rerun: bool = False)`
- `set_theme_text_color(color: Optional[str], rerun: bool = False)`
- `set_theme_font(font: Optional[str], rerun: bool = False)`

### Getting Theme Colors and Fonts

You can retrieve the current theme attributes using these functions:

- `get_theme_background_color() -> str`
- `get_theme_primary_color() -> str`
- `get_theme_secondary_background_color() -> str`
- `get_theme_text_color() -> str`
- `get_theme_font() -> str`

### Updating the Theme

You can update multiple theme attributes at once using the `update_theme` function:

```python
update_theme(background_color: Optional[str] = None,
             primary_color: Optional[str] = None,
             secondary_background_color: Optional[str] = None,
             text_color: Optional[str] = None,
             font: Optional[str] = None,
             rerun: bool = False)
```

### Theme Widgets

#### Custom Theme Widget

The custom theme widget allows users to manually select colors and fonts:

```python
custom_theme_widget(rerun: bool = True)
```

#### Predefined Theme Selector

The theme widget allows users to select from predefined themes:

```python
theme_widget(rerun: bool = True)
```

## Example

Here is an example of how to use the Streamlit Theme Manager in your Streamlit app:

```python
import streamlit as st
from theme_manager import custom_theme_widget, theme_widget

st.title("Streamlit Theme Manager")

# Display custom theme widget
custom_theme_widget()

# Display predefined theme selector
theme_widget()
```

## Predefined Themes

The predefined themes are stored in the `THEMES` dictionary and include the following:

- Beach
- Pineapple
- Peachy
- Tropical
- Mater
- Gastly
- Ocean
- Abyssal
- Green
- Sandy
- Sunset
- Midnight

Each theme includes the following attributes:
- `backgroundColor`
- `primaryColor`
- `secondaryBackgroundColor`
- `textColor`