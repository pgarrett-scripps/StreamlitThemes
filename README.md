# Streamlit-Themes

The `streamlit-themes` package provides a streamlined way to customize the visual appearance of Streamlit applications. 

**Note:** This package accesses the internal config directly at `st._config`, which is sort of a hack.
Use with caution. Also, updating the theme with `streamlit-themes` updates the theme for the entire Streamlit app
(including all users), so it's not suitable for multi-user apps.

## Installation

To install the `streamlit-themes` package, simply use pip:

```bash
pip install streamlit-themes
```

## Setup

If there is no custom theme provided in the .streamlit/config.toml file, then the getter functions
will return None values upon startup, and the custom color widget will default to a black values. 
To avoid this, it's best to specify as custom theme in the .streamlit/config.toml file. For example:

```toml
[theme]
primaryColor="#3282B8"
backgroundColor="#f1f0e8"
secondaryBackgroundColor="#eee0c9"
textColor="#45474b"
font="sans serif"
```

## Demo

![Alt Text](demo.gif)

## Basic Usage

Here's a basic example of how to use the `streamlit-themes` package:

```python
import streamlit_themes as st_themes

# Set a custom theme
st_themes.set_theme(
    background_color='#FFFFFF',
    primary_color='#1A73E8',
    secondary_background_color='#F1F3F4',
    text_color='#202124',
    font='sans serif'
)
```

## Functions

The following functions are available directly through `streamlit-themes`:

```python
import streamlit_themes as st_themes
```

- **`get_theme`**: Retrieves the current theme settings.
  ```python
  current_theme = st_themes.get_theme()
  ```

- **`set_theme`**: Sets the theme with specified parameters (background color, primary color, secondary background color, text color, font).
  ```python
  st_themes.set_theme(
      background_color='#FFFFFF',
      primary_color='#1A73E8',
      secondary_background_color='#F1F3F4',
      text_color='#202124',
      font='sans serif'
  )
  ```

- **`get_preset_theme`**: Retrieves the settings of a specified preset theme.
  ```python
  preset_theme = st_themes.get_preset_theme('Beach')
  ```

- **`set_preset_theme`**: Applies a specified preset theme.
  ```python
  st_themes.set_preset_theme('Beach')
  ```

- **`get_all_preset_themes`**: Retrieves all available preset themes.
  ```python
  all_presets = st_themes.get_all_preset_themes()
  ```

- **`custom_theme_widget`**: Creates a Streamlit widget for customizing and applying themes.
  ```python
  st_themes.custom_theme_widget()
  ```

- **`preset_theme_widget`**: Creates a Streamlit widget for selecting and applying preset themes.
  ```python
  st_themes.preset_theme_widget()
  ```
  
- **`Theme`**: A class that represents a theme with background color, primary color, secondary background color, text color, and font attributes.
  ```python
  theme = st_themes.Theme(
      background_color='#FFFFFF',
      primary_color='#1A73E8',
      secondary_background_color='#F1F3F4',
      text_color='#202124',
      font='sans serif'
  )
  ```
  
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
import streamlit_themes as st_themes

# Directly apply a preset theme
st_themes.set_preset_theme('Beach')
```