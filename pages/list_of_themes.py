import streamlit as st
import pandas as pd

from streamlit_themes import get_all_preset_themes

themes = get_all_preset_themes()

data = []
for key, theme in themes.items():
    data.append({
        'Name': key,
        'Primary Background Color': theme.background_color,
        'Secondary Background Color': theme.secondary_background_color,
        'Primary Color': theme.primary_color,
        'Text Color': theme.text_color,
        'Font': theme.font
    })

df = pd.DataFrame(data)

st.header("Predefined Themes")
#st.dataframe(df, use_container_width=True)

# color the cell according to thier hex value
def color_hex(val):
    return f"background-color: {val}"

colored_df = df.style.applymap(color_hex, subset=['Primary Background Color', 'Secondary Background Color', 'Primary Color', 'Text Color'])
st.dataframe(colored_df,
             use_container_width=True,
             hide_index=True,
             column_config={
                 'Name': st.column_config.TextColumn(width='small'),
                    'Primary Background Color': st.column_config.TextColumn(width='small'),
                    'Secondary Background Color': st.column_config.TextColumn(width='small'),
                    'Primary Color': st.column_config.TextColumn(width='small'),
                    'Text Color': st.column_config.TextColumn(width='small'),
                    'Font': st.column_config.TextColumn(width='small'),
             }
)

