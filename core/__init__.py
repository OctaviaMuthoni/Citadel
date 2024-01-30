import os
from enum import Enum


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


class ImageComponentMode(Enum):
    PREVIEW = "preview"
    UPLOAD = "upload"


class MessageSeverity:
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    SUCCESS = "success"