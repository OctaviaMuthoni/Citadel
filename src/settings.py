from PySide6.QtCore import QSettings


class Settings(QSettings):
    def __init__(self):
        super(Settings, self).__init__("Falcon", "Citadel")

        self.setValue("application", "")
        self.setValue("database", "")
        self.setValue("printer", "")
        self.setValue("user", "")

    def edit_settings(self, setting, value):
        self.setValue(setting, value)

    def get_settings(self, settings, default):
        return self.value(settings, default)

    def get_group_settings(self, group):
        settings = {}
        self.beginGroup(group)
        keys = self.childKeys()

        for key in keys:
            setting_value = self.value(key)
            settings[key] = setting_value
        self.endGroup()

        return settings


