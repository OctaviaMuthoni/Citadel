import os
from enum import Enum
# from .theme import ThemeManager

# constants
ICON_SIZE = 30

# path constants
STATIC_FILES_BASE_PATH = os.path.join(os.getenv('APPDATA'), 'Citadexx')
LOGS_PATH = os.path.join(os.getenv('APPDATA'), 'Citadexx', 'logs')
IMAGES_PATH = os.path.join(os.getenv('APPDATA'), 'Citadexx', 'images')
STYLES_PATH = os.path.join(os.getenv('APPDATA'), 'Citadexx', 'stylesheets')


class Colors:
    WARNING = "#E0DE30"
    ERROR = "#F71821"
    INFO = "#327AF7"
    SUCCESS = "#0BC24A"
    PRIMARY = "#0598A8"
    SECONDARY = ""
    ACCENT = ""
    ICON_COLOR = "#3AC1F7"
    ALTERNATE_ICON_COLOR = "#f1f1f1"
    LINKS_COLOR = "#1EA0F7"
    SIDE_BAR_COLOR = "#780598A8"
    PRIMARY_TEXT_COLOR = "#0598A8"
    ALTERNATE_TEXT_COLOR = "#f1f1f1"


class ImageComponentMode(Enum):
    PREVIEW = "preview"
    UPLOAD = "upload"


class MessageSeverity:
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    SUCCESS = "success"