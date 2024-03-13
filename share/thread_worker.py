from PySide6.QtCore import Slot, QRunnable


class Worker(QRunnable):

    def __init__(self, target, *args, **kwargs):
        super().__init__()

        self.target = target
        self.args = args
        self.kwargs = kwargs

    @Slot
    def run(self):
        self.target(*self.args, **self.kwargs)
