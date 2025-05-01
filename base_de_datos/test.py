# from modelo.VO.categoriasVO import CategoriasVO
# from conexiondb import conectar_cliente


# class CategoriasDAO:
#     def __init__(self):
#         self.cliente = conectar_cliente()
#         self.coleccion = self.cliente.BlocDB.categorias

#     def insertar_categoria(self, categoria: CategoriasVO) -> bool:
#         documento = {
#             "id": categoria.id,
#             "nombre_categoria": categoria.nombre_categoria
#         }
#         try:
#             self.coleccion.insert_one(
#                 documento)
#             return True
#         except:
#             print("Error al Insertar Categoria")
#             return False

#     def leer_categoria(self):
#         lista = []
#         categoria = self.coleccion.find()

#         for row in categoria:
#             lista.append(row)

#         return lista

#     def buscar_categoria_id(self, id):
#         lista = []
#         categoria = self.coleccion.find_one({"id": id})
#         lista.append(categoria["id"])
#         lista.append(categoria["nombre_categoria"])

#         return lista

#     def actualizar_categoria(self, categoria: CategoriasVO):
#         documento = {
#             "$set": {
#                 "nombre_categoria": categoria.nombre_categoria
#             }
#         }
#         try:
#             self.coleccion.update_one({"id": categoria.id},
#                                       documento)
#             return True
#         except Exception as e:
#             print("Error al insertar Categoria", e)
#             return False

#     def eliminar_categoria(self, id: int):
#         try:
#             self.coleccion.delete_one({"id": id})
#             return True
#         except Exception as e:
#             print("Error al eliminar", e)
#             return False


# dao = CategoriasDAO()
# print(dao.leer_categoria())


# NOTA IMPORTANTE PARA MANJEAR LOS LEER
#  for categoria in lista:
# print(categoria["id"], categoria["nombre_categoria"])

# NOTA IMPORTANTE PARA ACTUALIZAR/ELIMINAR
# dao.actualizar_categoria(categoria=CategoriasVO(
#   id=2, nombre_categoria="Papas"))


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from modelo.DAO.categoriasDAO import CategoriasDAO
from modelo.DAO.postsDAO import PostsDAO
from modelo.DAO.etiquetasDAO import EtiquetasDAO as EtiquetasDAO
from modelo.DAO.posts_etiquetadosDAO import Posts_EtiquetassDAO
from modelo.DAO.usuariosDAO import UsuariosDAO as UsuariosDAO
from modelo.DAO.comentariosDAO import ComentariosDAO as ComentariosDAO


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
        posts_etiquetados = Posts_EtiquetassDAO().leer_categoria()

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
