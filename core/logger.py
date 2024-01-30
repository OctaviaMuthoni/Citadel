import os
import logging
import datetime


class AppLogger:
    def __init__(self):
        # Set up the logging directory
        self.log_dir = os.path.join(os.getenv('APPDATA'), 'Musoni', 'logs')
        os.makedirs(self.log_dir, exist_ok=True)

        # Set up the app error logging
        self.app_logger = logging.getLogger('app_logger')
        app_log_file = os.path.join(self.log_dir, 'app.log')
        app_handler = logging.FileHandler(app_log_file)
        app_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        app_handler.setFormatter(app_formatter)
        self.app_logger.addHandler(app_handler)
        self.app_logger.setLevel(logging.INFO)

        # Set up the user action logging
        self.user_logger = logging.getLogger('user_logger')
        user_log_file = os.path.join(self.log_dir, 'user.log')
        user_handler = logging.FileHandler(user_log_file)
        user_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        user_handler.setFormatter(user_formatter)
        self.user_logger.addHandler(user_handler)
        self.user_logger.setLevel(logging.INFO)

    def log_user_action(self, user: str, action: str, description: str):
        log_message = f"{datetime.datetime.now().strftime('%Y-%m-%d')} | {datetime.datetime.now().strftime('%H:%M:%S')} | {user} | {action} | {description}"
        self.user_logger.info(log_message)

    def log_error(self, error_code: int, message: str, traceback: str):
        log_message = f"{datetime.datetime.now().strftime('%Y-%m-%d')} | {datetime.datetime.now().strftime('%H:%M:%S')} | {error_code} | {message} | {traceback}"
        self.app_logger.error(log_message)

