import dataclasses
from typing import Dict


@dataclasses.dataclass
class Theme:
    background_color: str
    primary_color: str
    secondary_background_color: str
    text_color: str
    font: str

    @classmethod
    def from_python_dict(cls, theme_dict: Dict[str, str]):
        return cls(
            background_color=theme_dict['background_color'],
            primary_color=theme_dict['primary_color'],
            secondary_background_color=theme_dict['secondary_background_color'],
            text_color=theme_dict['text_color'],
            font=theme_dict['font']
        )

    @classmethod
    def from_toml_dict(cls, theme_dict: Dict[str, str]):
        return cls(
            background_color=theme_dict['backgroundColor'],
            primary_color=theme_dict['primaryColor'],
            secondary_background_color=theme_dict['secondaryBackgroundColor'],
            text_color=theme_dict['textColor'],
            font=theme_dict['font']
        )

    @classmethod
    def from_dict(cls, theme_dict: Dict[str, str]):
        try:
            return cls.from_toml_dict(theme_dict)
        except KeyError:
            return cls.from_python_dict(theme_dict)

    @classmethod
    def from_config_string(cls, config_string: str):
        theme = {}
        for line in config_string.split("\n"):
            if line.startswith("[theme]"):
                continue
            key, value = line.split("=")
            theme[key] = value.strip('"')

        return cls(
            background_color=theme['backgroundColor'],
            primary_color=theme['primaryColor'],
            secondary_background_color=theme['secondaryBackgroundColor'],
            text_color=theme['textColor'],
            font=theme['font']
        )

    def to_dict(self) -> Dict[str, str]:
        return {
            'background_color': self.background_color,
            'primary_color': self.primary_color,
            'secondary_background_color': self.secondary_background_color,
            'text_color': self.text_color,
            'font': self.font
        }

    def to_toml_dict(self) -> Dict[str, str]:
        return {
            'backgroundColor': self.background_color,
            'primaryColor': self.primary_color,
            'secondaryBackgroundColor': self.secondary_background_color,
            'textColor': self.text_color,
            'font': self.font
        }

    def __str__(self):
        return str(self.to_dict())

    def to_streamlit_config_string(self) -> str:
        return (
            "[theme]\n"
            f'primaryColor="{self.primary_color}"\n'
            f'backgroundColor="{self.background_color}"\n'
            f'secondaryBackgroundColor="{self.secondary_background_color}"\n'
            f'textColor="{self.text_color}"\n'
            f'font="{self.font}"'
        )