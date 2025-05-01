import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from modelo.DAO.categoriasDAO import CategoriasDAO
from modelo.DAO.postsDAO import PostsDAO
from modelo.DAO.etiquetasDAO import EtiquetasDAO as EtiquetasDAO
from modelo.DAO.posts_etiquetadosDAO import PostEtiquetadosVO as PostsEtiquetadosDAO
from modelo.DAO.usuariosDAO import UsuariosDAO as UsuariosDAO
from modelo.DAO.comentariosDAO import ComentariosDAO as ComentariosDAO


class Dashboard(QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Dashboard del Blog")
        self.setGeometry(100, 100, 900, 700)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.figura = Figure(figsize=(10, 6))
        self.canvas = FigureCanvas(self.figura)
        self.layout.addWidget(self.canvas)

        self.info_layout = QHBoxLayout()
        self.layout.addLayout(self.info_layout)
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())
