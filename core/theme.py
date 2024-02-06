# """
#     This module manages the application theme and theme changes.
# """
# import importlib
# import os
# import re
#
# from PySide6.QtCore import QObject
#
# from core.settings import Settings
#
#
# class ThemeManager(QObject):
#     def __init__(self):
#         super(ThemeManager, self).__init__()
#
#         self.settings = Settings()
#
#     def load_theme(self, theme):
#         # dynamically import theme
#         try:
#             theme_module = importlib.import_module(f'themes.{theme.lower()}')
#             return theme_module
#         except ImportError:
#             print(f"Error: Theme '{theme}' not found.")
#             return None
#
#     def compile_theme(self):
#         # Load theme
#         theme = self.load_theme()
#
#         # Read stylesheet
#         compiled = ""
#         with open('themes/base.css') as stylesheet:
#             # Use a regex pattern to match placeholders like [SOME_VAR]
#             pattern = re.compile(r"\[([^\[\]]+)]")
#
#             # Iterate through each line in the stylesheet
#             for line in stylesheet:
#                 # Find all matches of the pattern in the line
#                 found_vars = pattern.findall(line)
#
#                 # Replace placeholders with actual values from the theme
#                 for found_var in found_vars:
#                     if hasattr(theme, found_var):
#                         val = getattr(theme, found_var)
#                         line = line.replace(f"[{found_var}]", val)
#
#                 # Append the modified line to the compiled CSS
#                 compiled += line
#
#         return compiled
#
#     def save_theme(self, compiled_styles, theme):
#         theme_directory = os.path.join('resources', theme.theme_name.lower())
#         os.makedirs(theme_directory, exist_ok=True)
#
#         # Save the compiled styles to a file
#         file_path = os.path.join(theme_directory, 'styles.qss')
#         with open(file_path, 'w') as theme_file:
#             theme_file.write(compiled_styles)
#
#         print(f"Compiled styles saved to: {file_path}")
import json
import os
import re


def load_themes():

    themes = dict()
    themes_dir = os.path.join("themes")

    # check if themes directory exist
    if os.path.exists(themes_dir):
        # get all files in the directory of type JSON
        # pathlib.Path.match(pathlib.Path(themes_dir), "*")
        for dirpath, dirnames, filenames in os.walk(themes_dir):
            # read the theme files.
            for filename in filenames:
                file, ext = filename.split('.')
                if ext == 'json':
                    with open(os.path.join(dirpath, filename)) as theme:
                        themes[file] = json.loads(theme.read())
    else:
        print("directory does not exist")

    return themes

def compile_theme():
    themes = load_themes()
    for theme, theme_data in themes.items():
        print("Compiling", theme)
        styles_path = os.path.join("resources/stylesheets", f"{theme}.qss")

        compiled = ''
        with open("resources/stylesheets/base.qss") as base:
            pattern = re.compile(r"\[([^\[\]]+)]")
            # Iterate through each line in the stylesheet
            for line in base:
                # Find all matches of the pattern in the line
                found_vars = pattern.findall(line)

                # Replace placeholders with actual values from the theme
                for var in found_vars:
                    print(var)
                    # val = (theme_data, var)
                    # print(val)
                    if var in theme_data.keys():
                        print("got here")
                        val = theme_data[var]
                        line = line.replace(f"[{var}]", val)

                # Append the modified line to the compiled CSS
                compiled += line
                print("Compiled", theme)
                save(styles_path, compiled)


def save(path, styles):
    print("Saving theme...")
    if os.path.exists(path):
        with open(path, 'w') as new_style:
            new_style.write(styles)
    else:
        with open(path, 'a') as new_style:
            new_style.write(styles)
    print("Saved theme.")

# compile_theme()