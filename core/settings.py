from PySide6.QtCore import QSettings, Signal

from configparser import ConfigParser

parser = ConfigParser()
parser.read("config.ini")


def load_defaults():
    _settings = {}
    sections = parser.sections()
    for section in sections:
        options = parser.options(section)
        _section_settings = dict()
        for option in options:
            _section_settings[option] = parser.get(section, option)
        _settings[section.lower()] = _section_settings

    return _settings


default_settings = load_defaults()


class Settings(QSettings):
    valueChanged = Signal(tuple)
    themeChanged = Signal(str)

    def __init__(self):
        super(Settings, self).__init__("Falcon", "Citadexx")

    def edit_settings(self, key, value):
        self.setValue(key, value)
        self.valueChanged.emit((key, value,))

    def set_theme(self, theme):
        self.beginGroup('application')
        self.setValue('theme', theme)
        self.themeChanged.emit(theme)
        self.endGroup()

    def get_settings(self, group, key):
        self.beginGroup(group)
        s = self.value(key, default_settings[group][key])
        self.endGroup()
        return s

    def get_group_settings(self, group):
        settings = {}
        self.beginGroup(group)
        keys = self.childKeys()

        for key in keys:
            setting_value = self.value(key, default_settings[group][key])
            settings[key] = setting_value
        self.endGroup()

        return settings
