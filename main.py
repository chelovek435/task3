from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt
import sys
import random
from u import Ui_Form


class main(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.draw_btn.clicked.connect(self.trigger_paint)

    def trigger_paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if not self.do_paint:
            return
        qp = QPainter(self)
        self.draw_circle(qp)
        self.do_paint = False

    def draw_circle(self, qp: QPainter):
        qp.setBrush(QColor(random.randint(0, 0xFFFFFF)))
        d = random.randint(20, 200)
        x = random.randint(0, self.width() - d)
        y = random.randint(50, self.height() - d)
        qp.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main()
    window.show()
    app.exec()
