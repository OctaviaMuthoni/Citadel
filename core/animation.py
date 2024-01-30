from PySide6.QtCore import QPropertyAnimation, QEasingCurve


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
    def __init__(self, target, property_name=b"pos"):
        super(SlideInAnimation, self).__init__(target, property_name)
        # Customize SlideInAnimation properties here
        self.setEndValue(target.pos() - target.rect().width())


class SlideOutAnimation(QPropertyAnimation):
    def __init__(self, target, property_name=b"pos"):
        super(SlideOutAnimation, self).__init__(target, property_name)
        # Customize SlideOutAnimation properties here
        self.setEndValue(target.pos() + target.rect().width())


class BounceAnimation(QPropertyAnimation):
    def __init__(self, target, property_name=b"geometry"):
        super(BounceAnimation, self).__init__(target, property_name)
        # Customize BounceAnimation properties here
        self.setKeyValueAt(0, target.geometry())
        self.setKeyValueAt(0.2, target.geometry().adjusted(-10, -10, 10, 10))
        self.setKeyValueAt(0.4, target.geometry())
        self.setKeyValueAt(0.6, target.geometry().adjusted(-10, -10, 10, 10))
        self.setKeyValueAt(0.8, target.geometry())
        self.setEndValue(target.geometry())


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
