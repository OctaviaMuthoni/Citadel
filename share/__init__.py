import os

from .config import load_settings
from .encryption import hash_password

# constants
ICON_SIZE = 30

# path constants
STATIC_FILES_BASE_PATH = os.path.join(os.getenv('APPDATA'), 'Citadexx')
LOGS_PATH = os.path.join(os.getenv('APPDATA'), 'Citadexx', 'logs')
IMAGES_PATH = os.path.join(os.getenv('APPDATA'), 'Citadexx', 'images')
STYLES_PATH = os.path.join(os.getenv('APPDATA'), 'Citadexx', 'styles')


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


AUDIO_FORMATS = [".mp3", ".ogg", ".wav"]
VIDEO_FORMATS = [".mp4", ".avi", ".mov", ".mkv"]


class MaterialFormat:
    AUDIO = "Audio"
    VIDEO = "Video"
    PRINT = "Print"
    SOFT_COPY = "soft copy"


class BillType:
    REGISTRATION = "Registration"
    ACTIVATION = "Activation"
    OVERDUE = "Overdue"
    LOSS_N_DAMAGE = "Loss & Damages"


class Gender:
    FEMALE = "female",
    MALE = "male"
    OTHER = "other"


class Status:
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    TERMINATED = "Terminated"
    SUSPENDED = "Suspended"


class Grades:
    # pre school
    PLAY_GROUP = "Grade 1"
    PP_1 = "Grade 1"
    PP_2 = "Grade 1"

    # lower primary
    GRADE_1 = "Grade 1"
    GRADE_2 = "Grade 1"
    GRADE_3 = "Grade 1"

    # upper primary
    GRADE_4 = "Grade 1"
    GRADE_5 = "Grade 1"
    GRADE_6 = "Grade 1"

    # junior school
    GRADE_7 = "Grade 1"
    GRADE_8 = "Grade 1"
    GRADE_9 = "Grade 1"

    # senior school
    GRADE_10 = "Grade 1"
    GRADE_11 = "Grade 1"
    GRADE_12 = "Grade 1"
