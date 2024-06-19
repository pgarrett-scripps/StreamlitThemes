# Streamlit-Themes

The `streamlit-themes` package provides a streamlined way to customize the visual appearance of Streamlit applications. 

**Note:** This package accesses the internal config at `st._config`, and is likely to break with future Streamlit updates. 
Use with caution. Also, updating the theme with `streamlit-themes` updates the theme for the entire Streamlit app
(including all users), so it's not suitable for multi-user apps.

## Installation

To install the `streamlit-themes` package, simply use pip:

```bash
pip install streamlit-themes
```

## Demo

![Alt Text](demo.gif)

## Basic Usage

Here's a basic example of how to use the `streamlit-themes` package:

```python
import streamlit_themes as st_theme

# Set a custom theme
st_theme.set_theme(
    background_color='#FFFFFF',
    primary_color='#1A73E8',
    secondary_background_color='#F1F3F4',
    text_color='#202124',
    font='sans serif'
)
```

## Functions

The following functions are available directly through the `__init__.py` file:

- `get_theme`: retrieves the current theme settings.
- `set_theme`: Sets the theme with given parameters.
- `get_preset_theme`: Retrieves a preset theme.
- `set_preset_theme`: Sets a preset theme.
- `get_all_preset_themes`: Retrieves all preset themes.
- `custom_theme_widget`: Creates a custom theme widget for user interaction.
- `preset_theme_widget`: Creates a preset theme widget for user interaction.
- `Theme`: Dataclass for storing themes.

Here are the preset theme keys available in the `constants.py` file:


## Preset Themes

The `streamlit-themes` package provides a set of preset keys that can be used to quickly apply predefined themes. 

### Available Preset Keys

- `Beach`
- `Pineapple`
- `Peachy`
- `Tropical`
- `Mater`
- `Gastly`
- `Ocean`
- `Abyssal`
- `Green`
- `Sandy`
- `Sunset`
- `Midnight`

### Example Usage

```python
import streamlit_themes as st_theme

# Directly apply a preset theme
st_theme.set_preset_theme('Beach')
```