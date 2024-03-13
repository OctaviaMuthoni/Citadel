import os
import typing

import qtawesome as qta
from PIL import Image
from PySide6.QtCore import QSize, Signal, Qt
from PySide6.QtGui import QDragEnterEvent, QDropEvent, QPixmap
from PySide6.QtWidgets import QVBoxLayout, QLabel, QCommandLinkButton, QFrame, QFileDialog, QWidget, QLineEdit, \
    QHBoxLayout, QSizePolicy


class ImageWidget(QFrame):
    # declare signals
    modeChangedSignal = Signal(typing.Any)

    # create image widget mode class
    class ImageWidgetMode:
        PREVIEW = "preview"
        UPLOAD = "upload"

    def __init__(self, mode: ImageWidgetMode = ImageWidgetMode.UPLOAD, size=QSize(200, 200)):
        super(ImageWidget, self).__init__()

        # initialize class variables
        self.mode = mode
        self.image_size = size

        # image preview label
        self.image_preview = QLabel("Drop Here")
        self.image_preview.setObjectName("image-preview")
        self.image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_preview.setScaledContents(True)
        self.image_preview.setFixedSize(self.image_size)

        # upload button
        self.upload_btn = QCommandLinkButton("Upload")
        self.upload_btn.clicked.connect(self.upload_image)

        # image path line edit
        self.image_path_edit = QLineEdit()
        self.image_path_edit.setPlaceholderText("paste the image path here.")

        # upload options widget
        self.upload_widget = QFrame()
        u_layout = QVBoxLayout(self.upload_widget)
        u_layout.addWidget(self.upload_btn)
        u_layout.addWidget(self.image_path_edit)

        # widget layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.image_preview)
        layout.addWidget(self.upload_widget)

        self.setObjectName("image-widget")
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # file upload dialog
        self.file_dialog = QFileDialog()
        self.file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        self.file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)

        self.change_mode(self.mode)
        self.modeChangedSignal.connect(self.change_mode)
        self.image_path_edit.textChanged.connect(self.update_image)

        self.setFixedWidth(self.image_size.width() + 20)

    def change_mode(self, mode):
        self.mode = mode
        if mode == self.ImageWidgetMode.PREVIEW:
            self.upload_widget.setHidden(True)
            self.setAcceptDrops(False)
        elif mode == self.ImageWidgetMode.UPLOAD:
            pixmap = qta.icon("fa.user-circle", color="#450598A8").pixmap(self.image_size * 0.75)
            self.image_preview.setPixmap(pixmap)
            self.image_preview.setScaledContents(False)
            self.upload_widget.setVisible(True)
            self.setAcceptDrops(True)

    def upload_image(self):
        f_name = self.file_dialog.getOpenFileName(filter="*.png *.jpg *.jpeg")[0]
        self.image_path_edit.setText(f_name)

    def update_image(self, path_: str):
        pixmap = QPixmap(path_)
        self.image_preview.setPixmap(pixmap)
        self.image_preview.setScaledContents(True)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        mime_data = event.mimeData()
        if mime_data.hasUrls() and mime_data.urls()[0].isLocalFile():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent) -> None:
        mime_data = event.mimeData()
        file_path = mime_data.urls()[0].toLocalFile()
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            self.image_path_edit.setText(file_path)
            event.accept()
