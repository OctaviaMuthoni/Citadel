from PySide6.QtCore import QSettings, Signal


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

    def get_settings(self, key, default):
        return self.value(key, default)

    def get_group_settings(self, group):
        settings = {}
        self.beginGroup(group)
        keys = self.childKeys()

        for key in keys:
            setting_value = self.value(key)
            settings[key] = setting_value
        self.endGroup()

        return settings


