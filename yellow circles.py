import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow circles.ui', self)
        self.btn.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        size = random.randint(1, 200)
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(random.randint(size, 832 - size), random.randint(size, 626 - size), size, size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
