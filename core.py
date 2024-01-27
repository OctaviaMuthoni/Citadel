import os
from enum import Enum


# constants
ICON_SIZE = 30

# path constants
STATIC_FILES_BASE_PATH = os.path.join(os.getenv('APPDATA'), 'Citadel')
LOGS_PATH = os.path.join(os.getenv('APPDATA'), 'Citadel', 'logs')
IMAGES_PATH = os.path.join(os.getenv('APPDATA'), 'Citadel', 'images')
STYLES_PATH = os.path.join(os.getenv('APPDATA'), 'Citadel', 'stylesheets')

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

# class Icons:
#     # social icons
#     WEBSITE = qta.icon("ph.globe", color="#0589a8")
#     FACEBOOK = qta.icon("ph.facebook-logo-light", color="#0589a8")
#     TWITTER = qta.icon("ph.twitter-logo-light", color="#0589a8")
#     INSTAGRAM = qta.icon("ph.instagram-logo-light", color="#0589a8")
#     YOUTUBE = qta.icon("ph.youtube-logo-light", color="#0589a8")
#
#     # general crud operations icons
#     EDIT = qta.icon("ph.globe", color="#0589a8")
#     DELETE = qta.icon("ph.globe", color="#0589a8")
#     ADD = qta.icon("ph.globe", color="#0589a8")
#     LIST = qta.icon("ph.globe", color="#0589a8")
#
#     # user icons
#     LIST_USERS = qta.icon("ph.user-list-light", color="#0589a8")
#     ADD_USER = qta.icon("ph.user-plus-light", color="#0589a8")
#     REMOVE_USER = qta.icon("ph.user-minus-light", color="#0589a8")
#     EDIT_USER = qta.icon("ph.user-gear-light", color="#0589a8")
#     LOGIN_ICON = qta.icon("ph.lock-key-light")
#
#     # material icons
#     NEWSPAPERS = qta.icon("fa.newspaper-o", color="#0589a8")
#     JOURNALS = qta.icon("ph.globe", color="#0589a8")
#     ADD_MATERIAL = qta.icon("ph.globe", color="#0589a8")
#     REMOVE_MATERIAL = qta.icon("ph.globe", color="#0589a8")
#     EDIT_MATERIAL = qta.icon("ph.globe", color="#0589a8")
#     LIST_MATERIAL = qta.icon("ph.globe", color="#0589a8")
#
#     # members
#     SUSPEND = qta.icon("ph.globe", color="#0589a8")
#
#     # other icons
#     LOST = qta.icon("mdi.book-remove", color="#0589a8")
#     DAMAGED = qta.icon("ri.file-damage-fill", color="#0589a8")
#     FURNITURE = qta.icon("mdi.table-chair", color="#0589a8")
#     COMPUTERS = qta.icon("ri.computer-line", color="#0589a8")
#     CLEANING = qta.icon("ei.broom", color="#0589a8")
#     REPORTS = qta.icon("fa.bar-chart-o", color="#0589a8")
#     SETTINGS = qta.icon("ri.settings-3-fill", color="#0589a8")
#     MANAGEMENT = qta.icon("ei.cogs", color="#0589a8")
#
#     # contacts
#     EMAIL = qta.icon("mdi6.email-multiple-outline", color="#0589a8")
#     PHONE = qta.icon("ph.phone-light", color="#0589a8")
#     ADDRESS = qta.icon("mdi.home-city-outline", color="#0589a8")
#     CITY = qta.icon("fa5s.city", color="#0589a8")
#
#     # time schedule
#     CALENDAR = qta.icon("fa.calendar", color="#0589a8")
#     TIME = qta.icon("mdi.clock-time-seven-outline", color="#0589a8")
#     REFRESH = qta.icon("ei.refresh", color="#0589a8")
#
#     # Database Icons
#     DATABASE = qta.icon("ph.database-light", color="silver")
#     DB_BACKUP = qta.icon("mdi.database-clock")
#     DB_SETTINGS = qta.icon("mdi.database-cog")
#     DB_SYNC = qta.icon("mdi.cloud-refresh")
#
#     CARD = qta.icon("fa.address-card-o")
#     LOAN = qta.icon("ph.handshake-thin")
#     PAYMENT = qta.icon("ri.coins-line")
#
