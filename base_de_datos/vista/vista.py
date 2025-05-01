from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
                             QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QHBoxLayout)


class VistaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Administrador de Bases de Datos")
        self.setGeometry(0, 0, 1800, 1000)

        self.initUI()

    def initUI(self):

        self.w1 = dict()
        self.w2 = dict()
        self.w3 = dict()

        # ||||||||||||||||||||||||||||||||||||||||||||||||||||
        """Categoria"""

        self.w1['buscar_id_categoria_ipt'] = QLineEdit(self)
        self.w1['buscar_id_categoria_ipt'].setPlaceholderText("ID Categoria")
        self.w1['nombre_categoria_ipt'] = QLineEdit(self)
        self.w1['nombre_categoria_ipt'].setPlaceholderText(
            "Nombre de Categoria:")

        self.w1['crear_categoria_btn'] = QPushButton("Crear Categoria", self)
        self.w1['actualizar_categoria_btn'] = QPushButton(
            "Actualizar Categoria", self)
        self.w1['buscar_id_categoria_btn'] = QPushButton(
            "Buscar Categoria", self)
        self.w1['borrar_categoria_btn'] = QPushButton("Borrar Categoria", self)
        self.w1['leer_categoria_btn'] = QPushButton("Mostrar Categorias", self)

        self.w1['tabla_categoria'] = QTableWidget(self)
        self.w1['tabla_categoria'].setColumnCount(2)
        self.w1['tabla_categoria'].setHorizontalHeaderLabels(
            ["ID", "Categoria"])
        self.w1['tabla_categoria'].setFixedSize(600, 200)

        # |||||||||||||||||||||||||||||||||||||||||||||||||
        """Comentario"""

        self.w1['buscar_id_comentario_ipt'] = QLineEdit(self)
        self.w1['buscar_id_comentario_ipt'].setPlaceholderText("ID Comentario")
        self.w1['cuerpo_comentario_ipt'] = QLineEdit(self)
        self.w1['cuerpo_comentario_ipt'].setPlaceholderText(
            "Cuerpo de Comentario:")
        self.w1['id_us_comentario_ipt'] = QLineEdit(self)
        self.w1['id_us_comentario_ipt'].setPlaceholderText(
            "ID de usuario que comento:")
        self.w1['id_pos_comentario_ipt'] = QLineEdit(self)
        self.w1['id_pos_comentario_ipt'].setPlaceholderText(
            "ID de post:")

        self.w1['crear_comentario_btn'] = QPushButton("Crear comentario", self)
        self.w1['actualizar_comentario_btn'] = QPushButton(
            "Actualizar comentario", self)
        self.w1['buscar_id_comentario_btn'] = QPushButton(
            "Buscar Comentario", self)
        self.w1['borrar_comentario_btn'] = QPushButton(
            "Borrar Comentario", self)
        self.w1['leer_comentarios_btn'] = QPushButton(
            "Mostrar Comentarios", self)

        self.w1['tabla_comentarios'] = QTableWidget(self)
        self.w1['tabla_comentarios'].setColumnCount(4)
        self.w1['tabla_comentarios'].setHorizontalHeaderLabels(
            ["ID", "Cuerpo", "Usuario ID", "Post ID"])
        self.w1['tabla_comentarios'].setFixedSize(600, 200)

        # |||||||||||||||||||||||||||||||||||||||||||||||||
        """etiqueta"""

        self.w2['buscar_id_etiqueta_ipt'] = QLineEdit(self)
        self.w2['buscar_id_etiqueta_ipt'].setPlaceholderText("ID Etiqueta")
        self.w2['nombre_etiqueta_ipt'] = QLineEdit(self)
        self.w2['nombre_etiqueta_ipt'].setPlaceholderText(
            "Nombre de etiqueta:")

        self.w2['crear_etiqueta_btn'] = QPushButton("Crear etiqueta", self)
        self.w2['actualizar_etiqueta_btn'] = QPushButton(
            "Actualizar etiqueta", self)
        self.w2['buscar_id_etiqueta_btn'] = QPushButton(
            "Buscar etiqueta", self)
        self.w2['borrar_etiqueta_btn'] = QPushButton("Borrar etiqueta", self)
        self.w2['leer_etiqueta_btn'] = QPushButton("Mostrar etiqueta", self)

        self.w2['tabla_etiquetas'] = QTableWidget(self)
        self.w2['tabla_etiquetas'].setColumnCount(2)
        self.w2['tabla_etiquetas'].setHorizontalHeaderLabels(
            ["ID", "Nombre Etiqueta"])
        self.w2['tabla_etiquetas'].setFixedSize(600, 200)

        # |||||||||||||||||||||||||||||||||||||||||||||||||||
        """Post"""

        self.w2['buscar_id_post_ipt'] = QLineEdit(self)
        self.w2['buscar_id_post_ipt'].setPlaceholderText("ID Post")
        self.w2['titulo_post_ipt'] = QLineEdit(self)
        self.w2['titulo_post_ipt'].setPlaceholderText(
            "Nombre de post:")
        self.w2['fecha_post_ipt'] = QLineEdit(self)
        self.w2['fecha_post_ipt'].setPlaceholderText(
            "Fecha de posteo:")
        self.w2['contenido_post_ipt'] = QLineEdit(self)
        self.w2['contenido_post_ipt'].setPlaceholderText(
            "contenido:")
        self.w2['estatus_post_ipt'] = QLineEdit()
        self.w2['estatus_post_ipt'].setPlaceholderText(
            "estatus:")
        self.w2['id_us_post_ipt'] = QLineEdit()
        self.w2['id_us_post_ipt'].setPlaceholderText("ID de poster")
        self.w2['id_cat_post_ipt'] = QLineEdit()
        self.w2['id_cat_post_ipt'].setPlaceholderText("ID de categoria")

        self.w2['crear_post_btn'] = QPushButton("Crear post", self)
        self.w2['actualizar_post_btn'] = QPushButton(
            "Actualizar post", self)
        self.w2['buscar_id_post_btn'] = QPushButton(
            "Buscar etiqueta", self)
        self.w2['borrar_post_btn'] = QPushButton("Borrar post", self)
        self.w2['leer_post_btn'] = QPushButton("Mostrar post", self)

        self.w2['tabla_posts'] = QTableWidget(self)
        self.w2['tabla_posts'].setColumnCount(6)
        self.w2['tabla_posts'].setHorizontalHeaderLabels(
            ["ID", "Titulo", "Fecha", "Contenido", "Estatus", "Usuario ID"])
        self.w2['tabla_posts'].setFixedSize(600, 200)

        # |||||||||||||||||||||||||||||||||||||||||||||||||||
        """Post Etiquetados"""

        self.w3['buscar_id_post_etiqueta_ipt'] = QLineEdit(self)
        self.w3['buscar_id_post_etiqueta_ipt'].setPlaceholderText(
            "ID Post Etiquetado")
        self.w3['id_pos_post_etiqueta_ipt'] = QLineEdit(self)
        self.w3['id_pos_post_etiqueta_ipt'].setPlaceholderText(
            "ID post etiquetado:")
        self.w3['id_eti_post_etiqueta_ipt'] = QLineEdit(self)
        self.w3['id_eti_post_etiqueta_ipt'].setPlaceholderText(
            "ID etiquetado del post:")

        self.w3['crear_post_etiqueta_btn'] = QPushButton(
            "Crear post etiquetado", self)
        self.w3['actualizar_etiqueta_btn'] = QPushButton(
            "Actualizar post etiquetado", self)
        self.w3['buscar_id_post_etiqueta_btn'] = QPushButton(
            "Buscar post etiquetado", self)
        self.w3['borrar_post_etiqueta_btn'] = QPushButton(
            "Borrar post etiquetado", self)
        self.w3['leer_post_etiqueta_btn'] = QPushButton(
            "Mostrar posts etiquetados", self)

        self.w3['tabla_post_etiquetas'] = QTableWidget(self)
        self.w3['tabla_post_etiquetas'].setColumnCount(3)
        self.w3['tabla_post_etiquetas'].setHorizontalHeaderLabels(
            ["ID", "ID_post", "ID_etiqueta"])
        self.w3['tabla_post_etiquetas'].setFixedSize(600, 200)

        # |||||||||||||||||||||||||||||||||||||||||||||||||||
        """Usuarios"""

        self.w3['buscar_id_usuario_ipt'] = QLineEdit(self)
        self.w3['buscar_id_usuario_ipt'].setPlaceholderText(
            "ID Usuario")
        self.w3['login_usuario_ipt'] = QLineEdit(self)
        self.w3['login_usuario_ipt'].setPlaceholderText(
            "Login")
        self.w3['password_usuario_ipt'] = QLineEdit(self)
        self.w3['password_usuario_ipt'].setPlaceholderText(
            "contraseña")
        self.w3['nickname_usuario_ipt'] = QLineEdit(self)
        self.w3['nickname_usuario_ipt'].setPlaceholderText(
            "apodo/nickname")
        self.w3['email_usuario_ipt'] = QLineEdit(self)
        self.w3['email_usuario_ipt'].setPlaceholderText(
            "correo-electronico")

        self.w3['crear_usuario_btn'] = QPushButton("Crear Usuario", self)
        self.w3['actualizar_usuario_btn'] = QPushButton(
            "Actualizar Usuario", self)
        self.w3['buscar_id_usuario_btn'] = QPushButton(
            "Buscar Usuario", self)
        self.w3['borrar_usuario_btn'] = QPushButton(
            "Borrar Usuario", self)
        self.w3['leer_usuario_btn'] = QPushButton(
            "Mostrar Usuarios", self)

        self.w3['tabla_usuario'] = QTableWidget(self)
        self.w3['tabla_usuario'].setColumnCount(5)
        self.w3['tabla_usuario'].setHorizontalHeaderLabels(
            ["ID", "Login", "PWD", "Apodo", "email"])
        self.w3['tabla_usuario'].setFixedSize(600, 200)
        self.w3['acc_dasboard_btn'] = QPushButton("Dashboard", self)

        self.layout_main = QHBoxLayout()
        self.layout_categoria_comentario = QVBoxLayout()
        self.layout_etiquetas_posts = QVBoxLayout()
        self.layout_postsetiquetados_usuarios = QVBoxLayout()

        for key, widget in self.w1.items():
            self.layout_categoria_comentario.addWidget(widget)

        for key, widget in self.w2.items():
            self.layout_etiquetas_posts.addWidget(widget)

        for key, widget in self.w3.items():
            self.layout_postsetiquetados_usuarios.addWidget(widget)

        self.layout_main.addLayout(self.layout_categoria_comentario)
        self.layout_main.addLayout(self.layout_etiquetas_posts)
        self.layout_main.addLayout(self.layout_postsetiquetados_usuarios)

        widget_principal = QWidget()
        widget_principal.setLayout(self.layout_main)
        self.setCentralWidget(widget_principal)
