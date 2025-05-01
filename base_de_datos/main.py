import sys
import os
from PyQt5.QtWidgets import QApplication
from vista.vista import Dashboard

if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    app = QApplication(sys.argv)
    ventana = Dashboard()
    ventana.show()
    sys.exit(app.exec_())