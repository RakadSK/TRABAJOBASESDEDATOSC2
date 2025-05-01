import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from modelo.DAO.categoriasDAO import CategoriasDAO
from modelo.DAO.postsDAO import PostsDAO
from modelo.DAO.etiquetasDAO import CategoriasDAO as EtiquetasDAO
from modelo.DAO.posts_etiquetadosDAO import CategoriasDAO as PostsEtiquetadosDAO
from modelo.DAO.usuariosDAO import CategoriasDAO as UsuariosDAO
from modelo.DAO.comentariosDAO import CategoriasDAO as ComentariosDAO

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard del Blog")
        self.setGeometry(100, 100, 900, 700)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.figure = Figure(figsize=(10, 6))
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.info_layout = QHBoxLayout()
        self.layout.addLayout(self.info_layout)

        self.contador_total("Posts", PostsDAO().leer_categoria())
        self.contador_total("Comentarios", ComentariosDAO().leer_categoria())
        self.contador_total("Usuarios", UsuariosDAO().leer_categoria())

        self.graficar_posts_por_categoria()
        self.graficar_etiquetas_mas_usadas()

    def contador_total(self, titulo, datos):
        total = len(datos)
        label = QLabel(f"<b>{titulo}:</b> {total}")
        self.info_layout.addWidget(label)

    def graficar_posts_por_categoria(self):
        categorias = CategoriasDAO().leer_categoria()
        posts = PostsDAO().leer_categoria()

        conteo = {cat["nombre_categoria"]: 0 for cat in categorias}
        for post in posts:
            for cat in categorias:
                if post["categoria_id"] == cat["id"]:
                    conteo[cat["nombre_categoria"]] += 1

        ejes = self.figure.add_subplot(121)
        ejes.clear()
        ejes.bar(conteo.keys(), conteo.values(), color='skyblue')
        ejes.set_title("Cantidad de Posts por Categoría")
        ejes.set_xlabel("Categoría")
        ejes.set_ylabel("Cantidad de Posts")
        ejes.tick_params(axis='x', rotation=45)

    def graficar_etiquetas_mas_usadas(self):
        etiquetas = EtiquetasDAO().leer_categoria()
        posts_etiquetados = PostsEtiquetadosDAO().leer_categoria()

        conteo_etiquetas = {et["nombre_etiqueta"]: 0 for et in etiquetas}
        for post_et in posts_etiquetados:
            for et in etiquetas:
                if post_et["etiqueta_id"] == et["id"]:
                    conteo_etiquetas[et["nombre_etiqueta"]] += 1

        ejes = self.figure.add_subplot(122)
        ejes.clear()
        etiquetas = list(conteo_etiquetas.keys())
        valores = list(conteo_etiquetas.values())
        ejes.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=140)
        ejes.set_title("Etiquetas más usadas")

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())
