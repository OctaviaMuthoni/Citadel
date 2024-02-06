import os
import typing

import qtawesome as qta
from PIL import Image
from PySide6.QtCore import QSize, Signal, Qt
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QPixmap
from PySide6.QtWidgets import QVBoxLayout, QLabel, QCommandLinkButton, QFrame, QFileDialog, QWidget

from core import ImageComponentMode


class ImageComponent(QFrame):
    imageChangeSignal = Signal(str)
    modeChangedSignal = Signal(typing.Any)

    def __init__(self, mode: ImageComponentMode = ImageComponentMode.PREVIEW, size=QSize(200, 200)):
        super(ImageComponent, self).__init__()

        self.mode = mode
        layout = QVBoxLayout(self)

        self.image_preview = QLabel("Drop Here")
        self.image_preview.setObjectName("preview-lbl")
        self.image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_preview.setScaledContents(True)
        self.image_preview.setFixedSize(size)

        self.upload_controls_widget = QWidget()
        upload_layout = QVBoxLayout(self.upload_controls_widget)
        upload_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.upload_btn = QCommandLinkButton("Upload")
        self.upload_btn.clicked.connect(self.upload_image)

        upload_layout.addWidget(self.upload_btn)

        layout.addWidget(self.image_preview)
        layout.addWidget(self.upload_controls_widget)

        self.imageChangeSignal.connect(self.update_image)
        self.setObjectName("image-upload")

        self.file_dialog = QFileDialog()
        self.file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        self.file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)

        self.change_mode(self.mode)
        self.modeChangedSignal.connect(self.change_mode)

    def change_mode(self, mode):
        self.mode = mode
        if mode == ImageComponentMode.PREVIEW:
            self.upload_controls_widget.setHidden(True)
            self.setAcceptDrops(False)
        elif mode == ImageComponentMode.UPLOAD:
            pixmap = qta.icon("ph.user-focus-thin", color="silver").pixmap(256)
            self.image_preview.setPixmap(pixmap)
            self.upload_controls_widget.setHidden(False)
            self.setAcceptDrops(True)

    def upload_image(self):
        f_name = self.file_dialog.getOpenFileName(filter="*.png *.jpg *.jpeg")[0]

        temp_preview_path = os.path.join("resources/images/temp/", "preview.png")
        with Image.open(f_name) as img:
            img.thumbnail((200, 200))

            img.save(temp_preview_path, format="PNG")
            self.imageChangeSignal.emit(temp_preview_path)

    def update_image(self, path_: str):
        pixmap = QPixmap(path_)
        self.image_preview.setPixmap(pixmap)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        mime_data = event.mimeData()
        if mime_data.hasUrls() and mime_data.urls()[0].isLocalFile():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent) -> None:
        mime_data = event.mimeData()
        file_path = mime_data.urls()[0].toLocalFile()
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            self.imageChangeSignal.emit(file_path)
            event.accept()
