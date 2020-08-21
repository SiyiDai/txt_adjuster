# coding: utf-8
from widgets import QtWidgets, WidgetMain
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    m = WidgetMain()
    m.show()
    sys.exit(app.exec_())
