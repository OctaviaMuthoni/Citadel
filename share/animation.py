from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect, QPoint
from PySide6.QtWidgets import QSizePolicy


class FontAnimation(QPropertyAnimation):
    def __init__(self, target, property_name=b"font_size"):
        super(FontAnimation, self).__init__(target, property_name)
        # Customize FontAnimation properties here


class GrowAnimation(QPropertyAnimation):
    def __init__(self, target, property_name=b"geometry"):
        super(GrowAnimation, self).__init__(target, property_name)
        # Customize GrowAnimation properties here
        self.setEndValue(target.geometry().adjusted(-10, -10, 10, 10))


class ShrinkAnimation(QPropertyAnimation):
    def __init__(self, target, property_name=b"geometry"):
        super(ShrinkAnimation, self).__init__(target, property_name)
        # Customize ShrinkAnimation properties here
        self.setEndValue(target.geometry().adjusted(10, 10, -10, -10))


class SlideInAnimation(QPropertyAnimation):
    def __init__(self, target, initial, final):
        super(SlideInAnimation, self).__init__(target, b"geometry")

        print(initial, final)

        self.setStartValue(initial)
        self.setEndValue(final)
        self.setDuration(1000)
        self.setEasingCurve(QEasingCurve.Type.InCurve)

    def slide_in(self):
        self.start()


class SlideOutAnimation(QPropertyAnimation):
    def __init__(self, target, property_name=b"pos"):
        super(SlideOutAnimation, self).__init__(target, property_name)
        # Customize SlideOutAnimation properties here
        self.setEndValue(target.pos() + target.rect().width())


class DockWidgetAnimation(QPropertyAnimation):
    def __init__(self, target, property_name=b"geometry"):
        super(DockWidgetAnimation, self).__init__(target, property_name)

        self.setDuration(1000)
        self.setStartValue(QRect(0, 0, target.sizeHint().width(), target.sizeHint().height()))
        self.setEndValue(QRect(0, 0, 0, target.sizeHint().height()))


class LoaderAnimation(QPropertyAnimation):
    def __init__(self, target, property_name=b"rotation"):
        super(LoaderAnimation, self).__init__(target, property_name)
        # Customize LoaderAnimation properties here
        self.setStartValue(0)
        self.setEndValue(360)


class SpinAnimation(QPropertyAnimation):
    def __init__(self, target, property_name=b"rotation"):
        super(SpinAnimation, self).__init__(target, property_name)
        # Customize SpinAnimation properties here
        self.setEasingCurve(QEasingCurve.OutBounce)
        self.setStartValue(0)
        self.setEndValue(360)


