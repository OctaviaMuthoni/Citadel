from configparser import ConfigParser, NoSectionError, ParsingError

from PySide6.QtCore import QSettings


def load_local_settings(section: str) -> dict:
    # declare settings dictionary
    settings = dict()

    # instantiate parser
    parser = ConfigParser()

    # parse config file
    try:
        parser.read('config.ini')
    except ParsingError as e:
        # TODO: implement logging for this error
        print("parsing error", e)

    options = []

    # ensure the target section exists
    try:
        # get options in the target section
        options = parser.options(section)
    except NoSectionError as e:
        # TODO: implement logging for this error
        print("Section does not exist", e)

    # get values for all section options
    if options:
        for option in options:
            val = parser.get(section, option)
            settings[option] = val

    return settings


def load_settings(group: str) -> dict:
    group = group.upper()

    # declare settings dictionary
    settings = dict()

    # create a settings object from PySide6.QtCore.QSettings
    settings_obj = QSettings("Lilly", "LMS")

    # start reading the target group.
    settings_obj.beginGroup(group)

    keys = settings_obj.childKeys()
    if keys:
        for key in keys:
            # get key value from the settings object which defaults to the local settings value.
            settings[key] = settings_obj.value(key, load_local_settings(group)[key])

    # update from the local settings in case some keys are missing
    settings.update(load_local_settings(group))

    settings_obj.endGroup()
    # end reading group

    # return the settings dictionary
    return settings

# TODO: implement setting a value for local settings


# TODO: implement setting a value for a system settings


# TODO: implement a function that synchronizes settings (both local and system wide)
