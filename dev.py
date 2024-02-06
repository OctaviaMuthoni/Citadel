# This module is a utility module that helps in my development.
# It watches the changes to theme directory and to base stylesheet and recompile the stylesheets
# import os

from PySide6.QtCore import QFileSystemWatcher

from core import theme

import os
import time
import threading
from core.theme import compile_theme


class FileWatcher:
    def __init__(self):

        self.files_to_watch = list()
        for dirname, _, filenames in os.walk('themes'):
            if filenames:
                for filename in filenames:
                    self.files_to_watch.append(os.path.join(dirname, filename))

        self.files_to_watch.append("resources/stylesheets/base.qss")

        self.file_modification_times = {file: self.get_file_modification_time(file) for file in self.files_to_watch}
        self.lock = threading.Lock()

    def start_watching(self):
        print("Watching ...")
        while True:
            time.sleep(1)
            with self.lock:
                for file_path in self.files_to_watch:
                    current_time = self.get_file_modification_time(file_path)
                    if current_time != self.file_modification_times[file_path]:
                        print("Compiling theme ... ")
                        theme.compile_theme()
                        self.file_modification_times[file_path] = current_time

    @staticmethod
    def get_file_modification_time(file_path):
        try:
            return os.path.getmtime(file_path)
        except FileNotFoundError:
            return None


# Paths to watch

# Initialize and start the file watcher
file_watcher = FileWatcher()
watcher_thread = threading.Thread(target=file_watcher.start_watching)
watcher_thread.start()

# Run the PySide6 application event loop to keep it running
from PySide6.QtCore import QCoreApplication

app = QCoreApplication([])
app.exec()


#
# watcher = QFileSystemWatcher(files_to_watch)
# watcher.fileChanged.connect(compile_theme)
