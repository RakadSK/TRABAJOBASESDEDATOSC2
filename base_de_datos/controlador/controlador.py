from modelo.DAO import categoriasDAO, comentariosDAO, etiquetasDAO, posts_etiquetadosDAO, postsDAO, usuariosDAO
from modelo.VO import categoriasVO, comentariosVO, etiquetasVO, posts_etiquetadosVO, postsVO, usuariosVO
from vista import vista
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
import sys


class ControladorGUI:
    def __init__(self):

        self.app = QApplication(sys.argv)
        self.ventana = vista.VistaPrincipal()

        self.CAT_DAO = categoriasDAO.CategoriasDAO()
        self.COM_DAO = comentariosDAO.ComentariosDAO()
        self.ETI_DAO = etiquetasDAO.EtiquetasDAO()
        self.POS_DAO = postsDAO.PostsDAO()
        self.USU_DAO = usuariosDAO.UsuariosDAO()
        self.POS_ETI_DAO = posts_etiquetadosDAO.Posts_EtiquetassDAO()

        self._setup_handlers()

    def _setup_handlers(self):

        self.ventana.w1['crear_categoria_btn'].clicked.connect(
            self.handler_insertar_categoria)
        self.ventana.w1['leer_categoria_btn'].clicked.connect(
            self.handler_leer_categorias)
        self.ventana.w1['actualizar_categoria_btn'].clicked.connect(
            self.handler_actualizar_categoria)
        self.ventana.w1['borrar_categoria_btn'].clicked.connect(
            self.handler_eliminar_categoria)
        self.ventana.w1['buscar_id_categoria_btn'].clicked.connect(
            self.handler_buscar_categoria)

        self.ventana.w1['crear_comentario_btn'].clicked.connect(
            self.handler_insertar_comentario)
        self.ventana.w1['leer_comentarios_btn'].clicked.connect(
            self.handler_leer_comentarios)
        self.ventana.w1['actualizar_comentario_btn'].clicked.connect(
            self.handler_actualizar_comentario)
        self.ventana.w1['borrar_comentario_btn'].clicked.connect(
            self.handler_eliminar_comentario)
        self.ventana.w1['buscar_id_comentario_btn'].clicked.connect(
            self.handler_buscar_comentario)

        self.ventana.w2['crear_etiqueta_btn'].clicked.connect(
            self.handler_insertar_etiqueta)
        self.ventana.w2['leer_etiqueta_btn'].clicked.connect(
            self.handler_leer_etiquetas)
        self.ventana.w2['actualizar_etiqueta_btn'].clicked.connect(
            self.handler_actualizar_etiqueta)
        self.ventana.w2['borrar_etiqueta_btn'].clicked.connect(
            self.handler_eliminar_etiqueta)
        self.ventana.w2['buscar_id_etiqueta_btn'].clicked.connect(
            self.handler_buscar_etiqueta)

        self.ventana.w2['crear_post_btn'].clicked.connect(
            self.handler_insertar_post)
        self.ventana.w2['leer_post_btn'].clicked.connect(
            self.handler_leer_posts)
        self.ventana.w2['actualizar_post_btn'].clicked.connect(
            self.handler_actualizar_post)
        self.ventana.w2['borrar_post_btn'].clicked.connect(
            self.handler_eliminar_post)
        self.ventana.w2['buscar_id_post_btn'].clicked.connect(
            self.handler_buscar_post)

        self.ventana.w3['crear_usuario_btn'].clicked.connect(
            self.handler_insertar_usuario)
        self.ventana.w3['leer_usuario_btn'].clicked.connect(
            self.handler_leer_usuarios)
        self.ventana.w3['actualizar_usuario_btn'].clicked.connect(
            self.handler_actualizar_usuario)
        self.ventana.w3['borrar_usuario_btn'].clicked.connect(
            self.handler_eliminar_usuario)
        self.ventana.w3['buscar_id_usuario_btn'].clicked.connect(
            self.handler_buscar_usuario)

        self.ventana.w3['crear_post_etiqueta_btn'].clicked.connect(
            self.handler_insertar_post_etiquetado)
        self.ventana.w3['leer_post_etiqueta_btn'].clicked.connect(
            self.handler_leer_posts_etiquetados)
        self.ventana.w3['actualizar_etiqueta_btn'].clicked.connect(
            self.handler_actualizar_post_etiquetado)
        self.ventana.w3['borrar_post_etiqueta_btn'].clicked.connect(
            self.handler_eliminar_post_etiquetado)
        self.ventana.w3['buscar_id_post_etiqueta_btn'].clicked.connect(
            self.handler_buscar_post_etiquetado)

    def handler_insertar_categoria(self):
        nombre_categoria = self.ventana.w1['nombre_categoria_ipt'].text()
        nuevo_id = self.crear_nuevo_id(self.CAT_DAO.leer_categoria())
        nueva_categoria = categoriasVO.CategoriasVO(
            id=nuevo_id, nombre_categoria=nombre_categoria)
        if self.CAT_DAO.insertar_categoria(nueva_categoria):
            print("Categoría insertada con éxito.")
            self.handler_leer_categorias()

    def handler_leer_categorias(self):
        categorias = self.CAT_DAO.leer_categoria()
        self.ventana.w1['tabla_categoria'].setRowCount(0)
        for categoria in categorias:
            row = self.ventana.w1['tabla_categoria'].rowCount()
            self.ventana.w1['tabla_categoria'].insertRow(row)
            self.ventana.w1['tabla_categoria'].setItem(
                row, 0, QTableWidgetItem(str(categoria["id"])))
            self.ventana.w1['tabla_categoria'].setItem(
                row, 1, QTableWidgetItem(categoria["nombre_categoria"]))

    def handler_actualizar_categoria(self):
        id_categoria = int(self.ventana.w1['buscar_id_categoria_ipt'].text())
        nombre_categoria = self.ventana.w1['nombre_categoria_ipt'].text()
        categoria_actualizada = categoriasVO.CategoriasVO(
            id=id_categoria, nombre_categoria=nombre_categoria)
        if self.CAT_DAO.actualizar_categoria(categoria_actualizada):
            print("Categoría actualizada con éxito.")
            self.handler_leer_categorias()

    def handler_eliminar_categoria(self):
        id_categoria = int(self.ventana.w1['buscar_id_categoria_ipt'].text())
        if self.CAT_DAO.eliminar_categoria(id_categoria):
            print("Categoría eliminada con éxito.")
            self.handler_leer_categorias()

    def handler_buscar_categoria(self):
        id_categoria = int(self.ventana.w1['buscar_id_categoria_ipt'].text())
        categoria = self.CAT_DAO.buscar_categoria_id(id_categoria)
        if categoria:

            self.ventana.w1['nombre_categoria_ipt'].setText(categoria[1])

    def handler_insertar_comentario(self):
        cuerpo_comentario = self.ventana.w1['cuerpo_comentario_ipt'].text()
        id_usuario = int(self.ventana.w1['id_us_comentario_ipt'].text())
        id_post = int(self.ventana.w1['id_pos_comentario_ipt'].text())
        nuevo_id = self.crear_nuevo_id(self.COM_DAO.leer_categoria())
        nuevo_comentario = comentariosVO.ComentariosVO(
            id=nuevo_id, cuerpo_comentario=cuerpo_comentario, usuario_id=id_usuario, post_id=id_post)
        if self.COM_DAO.insertar_categoria(nuevo_comentario):
            print("Comentario insertado con éxito.")
            self.handler_leer_comentarios()

    def handler_leer_comentarios(self):
        comentarios = self.COM_DAO.leer_categoria()
        self.ventana.w1['tabla_comentarios'].setRowCount(0)
        for comentario in comentarios:
            row = self.ventana.w1['tabla_comentarios'].rowCount()
            self.ventana.w1['tabla_comentarios'].insertRow(row)
            self.ventana.w1['tabla_comentarios'].setItem(
                row, 0, QTableWidgetItem(str(comentario["id"])))
            self.ventana.w1['tabla_comentarios'].setItem(
                row, 1, QTableWidgetItem(comentario["cuerpo_comentario"]))
            self.ventana.w1['tabla_comentarios'].setItem(
                row, 2, QTableWidgetItem(str(comentario["usuario_id"])))
            self.ventana.w1['tabla_comentarios'].setItem(
                row, 3, QTableWidgetItem(str(comentario["post_id"])))

    def handler_actualizar_comentario(self):
        id_comentario = int(self.ventana.w1['buscar_id_comentario_ipt'].text())
        cuerpo_comentario = self.ventana.w1['cuerpo_comentario_ipt'].text()
        id_usuario = int(self.ventana.w1['id_us_comentario_ipt'].text())
        id_post = int(self.ventana.w1['id_pos_comentario_ipt'].text())
        comentario_actualizado = comentariosVO.ComentariosVO(
            id=id_comentario, cuerpo_comentario=cuerpo_comentario, usuario_id=id_usuario, post_id=id_post)
        if self.COM_DAO.actualizar_categoria(comentario_actualizado):
            print("Comentario actualizado con éxito.")
            self.handler_leer_comentarios()

    def handler_eliminar_comentario(self):
        id_comentario = int(self.ventana.w1['buscar_id_comentario_ipt'].text())
        if self.COM_DAO.eliminar_categoria(id_comentario):
            print("Comentario eliminado con éxito.")
            self.handler_leer_comentarios()

    def handler_buscar_comentario(self):
        id_comentario = int(self.ventana.w1['buscar_id_comentario_ipt'].text())
        comentario = self.COM_DAO.buscar_categoria_id(id_comentario)
        if comentario:

            self.ventana.w1['cuerpo_comentario_ipt'].setText(comentario[1])
            self.ventana.w1['id_us_comentario_ipt'].setText(str(comentario[2]))
            self.ventana.w1['id_pos_comentario_ipt'].setText(
                str(comentario[3]))

    def handler_insertar_etiqueta(self):
        nombre_etiqueta = self.ventana.w2['nombre_etiqueta_ipt'].text()
        nuevo_id = self.crear_nuevo_id(self.ETI_DAO.leer_categoria())
        nueva_etiqueta = etiquetasVO.EtiquetasVO(
            id=nuevo_id, nombre_etiqueta=nombre_etiqueta)
        if self.ETI_DAO.insertar_categoria(nueva_etiqueta):
            print("Etiqueta insertada con éxito.")
            self.handler_leer_etiquetas()

    def handler_leer_etiquetas(self):
        etiquetas = self.ETI_DAO.leer_categoria()
        self.ventana.w2['tabla_etiquetas'].setRowCount(0)
        for etiqueta in etiquetas:
            row = self.ventana.w2['tabla_etiquetas'].rowCount()
            self.ventana.w2['tabla_etiquetas'].insertRow(row)
            self.ventana.w2['tabla_etiquetas'].setItem(
                row, 0, QTableWidgetItem(str(etiqueta["id"])))
            self.ventana.w2['tabla_etiquetas'].setItem(
                row, 1, QTableWidgetItem(etiqueta["nombre_etiqueta"]))

    def handler_actualizar_etiqueta(self):
        id_etiqueta = int(self.ventana.w2['buscar_id_etiqueta_ipt'].text())
        nombre_etiqueta = self.ventana.w2['nombre_etiqueta_ipt'].text()
        etiqueta_actualizada = etiquetasVO.EtiquetasVO(
            id=id_etiqueta, nombre_etiqueta=nombre_etiqueta)
        if self.ETI_DAO.actualizar_categoria(etiqueta_actualizada):
            print("Etiqueta actualizada con éxito.")
            self.handler_leer_etiquetas()

    def handler_eliminar_etiqueta(self):
        id_etiqueta = int(self.ventana.w2['buscar_id_etiqueta_ipt'].text())
        if self.ETI_DAO.eliminar_categoria(id_etiqueta):
            print("Etiqueta eliminada con éxito.")
            self.handler_leer_etiquetas()

    def handler_buscar_etiqueta(self):
        id_etiqueta = int(self.ventana.w2['buscar_id_etiqueta_ipt'].text())
        etiqueta = self.ETI_DAO.buscar_categoria_id(id_etiqueta)
        if etiqueta:

            self.ventana.w2['nombre_etiqueta_ipt'].setText(etiqueta[1])

    def handler_insertar_post(self):
        titulo = self.ventana.w2['titulo_post_ipt'].text()
        fecha_publicacion = self.ventana.w2['fecha_post_ipt'].text()
        contenido = self.ventana.w2['contenido_post_ipt'].text()
        estatus = self.ventana.w2['estatus_post_ipt'].text()
        id_usuario = int(self.ventana.w2['id_us_post_ipt'].text())
        id_categoria = int(self.ventana.w2['id_cat_post_ipt'].text())
        nuevo_id = self.crear_nuevo_id(self.POS_DAO.leer_categoria())
        nuevo_post = postsVO.PostsVO(id=nuevo_id, titulo=titulo, fecha_publicacion=fecha_publicacion,
                                     contenido=contenido, estatus=estatus, usuario_id=id_usuario, categoria_id=id_categoria)
        if self.POS_DAO.insertar_categoria(nuevo_post):
            print("Post insertado con éxito.")
            self.handler_leer_posts()

    def handler_leer_posts(self):
        posts = self.POS_DAO.leer_categoria()
        self.ventana.w2['tabla_posts'].setRowCount(0)
        for post in posts:
            row = self.ventana.w2['tabla_posts'].rowCount()
            self.ventana.w2['tabla_posts'].insertRow(row)
            self.ventana.w2['tabla_posts'].setItem(
                row, 0, QTableWidgetItem(str(post["id"])))
            self.ventana.w2['tabla_posts'].setItem(
                row, 1, QTableWidgetItem(post["titulo"]))
            self.ventana.w2['tabla_posts'].setItem(
                row, 2, QTableWidgetItem(post["fecha_publicacion"]))
            self.ventana.w2['tabla_posts'].setItem(
                row, 3, QTableWidgetItem(post["contenido"]))
            self.ventana.w2['tabla_posts'].setItem(
                row, 4, QTableWidgetItem(post["estatus"]))
            self.ventana.w2['tabla_posts'].setItem(
                row, 5, QTableWidgetItem(str(post["usuario_id"])))

    def handler_actualizar_post(self):
        id_post = int(self.ventana.w2['buscar_id_post_ipt'].text())
        titulo = self.ventana.w2['titulo_post_ipt'].text()
        fecha_publicacion = self.ventana.w2['fecha_post_ipt'].text()
        contenido = self.ventana.w2['contenido_post_ipt'].text()
        estatus = self.ventana.w2['estatus_post_ipt'].text()
        id_usuario = int(self.ventana.w2['id_us_post_ipt'].text())
        id_categoria = int(self.ventana.w2['id_cat_post_ipt'].text())
        post_actualizado = postsVO.PostsVO(id=id_post, titulo=titulo, fecha_publicacion=fecha_publicacion,
                                           contenido=contenido, estatus=estatus, usuario_id=id_usuario, categoria_id=id_categoria)
        if self.POS_DAO.actualizar_categoria(post_actualizado):
            print("Post actualizado con éxito.")
            self.handler_leer_posts()

    def handler_eliminar_post(self):
        id_post = int(self.ventana.w2['buscar_id_post_ipt'].text())
        if self.POS_DAO.eliminar_categoria(id_post):
            print("Post eliminado con éxito.")
            self.handler_leer_posts()

    def handler_buscar_post(self):
        id_post = int(self.ventana.w2['buscar_id_post_ipt'].text())
        post = self.POS_DAO.buscar_categoria_id(id_post)
        if post:

            self.ventana.w2['titulo_post_ipt'].setText(post[1])
            self.ventana.w2['fecha_post_ipt'].setText(post[2])
            self.ventana.w2['contenido_post_ipt'].setText(post[3])
            self.ventana.w2['estatus_post_ipt'].setText(post[4])
            self.ventana.w2['id_us_post_ipt'].setText(str(post[5]))
            self.ventana.w2['id_cat_post_ipt'].setText(str(post[6]))

    def handler_insertar_post_etiquetado(self):
        id_post = int(self.ventana.w3['id_pos_post_etiqueta_ipt'].text())
        id_etiqueta = int(self.ventana.w3['id_eti_post_etiqueta_ipt'].text())
        nuevo_id = self.crear_nuevo_id(self.POS_ETI_DAO.leer_categoria())
        nuevo_post_etiquetado = posts_etiquetadosVO.PostEtiquetadosVO(
            id=nuevo_id, post_id=id_post, etiqueta_id=id_etiqueta)
        if self.POS_ETI_DAO.insertar_categoria(nuevo_post_etiquetado):
            print("Post etiquetado insertado con éxito.")
            self.handler_leer_posts_etiquetados()

    def handler_leer_posts_etiquetados(self):
        posts_etiquetados = self.POS_ETI_DAO.leer_categoria()
        self.ventana.w3['tabla_post_etiquetas'].setRowCount(0)
        for post_etiquetado in posts_etiquetados:
            row = self.ventana.w3['tabla_post_etiquetas'].rowCount()
            self.ventana.w3['tabla_post_etiquetas'].insertRow(row)
            self.ventana.w3['tabla_post_etiquetas'].setItem(
                row, 0, QTableWidgetItem(str(post_etiquetado["id"])))
            self.ventana.w3['tabla_post_etiquetas'].setItem(
                row, 1, QTableWidgetItem(str(post_etiquetado["post_id"])))
            self.ventana.w3['tabla_post_etiquetas'].setItem(
                row, 2, QTableWidgetItem(str(post_etiquetado["etiqueta_id"])))

    def handler_actualizar_post_etiquetado(self):
        id_post_etiquetado = int(
            self.ventana.w3['buscar_id_post_etiqueta_ipt'].text())
        id_post = int(self.ventana.w3['id_pos_post_etiqueta_ipt'].text())
        id_etiqueta = int(self.ventana.w3['id_eti_post_etiqueta_ipt'].text())
        post_etiquetado_actualizado = posts_etiquetadosVO.PostEtiquetadosVO(
            id=id_post_etiquetado, post_id=id_post, etiqueta_id=id_etiqueta)
        if self.POS_ETI_DAO.actualizar_categoria(post_etiquetado_actualizado):
            print("Post etiquetado actualizado con éxito.")
            self.handler_leer_posts_etiquetados()

    def handler_eliminar_post_etiquetado(self):
        id_post_etiquetado = int(
            self.ventana.w3['buscar_id_post_etiqueta_ipt'].text())
        if self.POS_ETI_DAO.eliminar_categoria(id_post_etiquetado):
            print("Post etiquetado eliminado con éxito.")
            self.handler_leer_posts_etiquetados()

    def handler_buscar_post_etiquetado(self):
        id_post_etiquetado = int(
            self.ventana.w3['buscar_id_post_etiqueta_ipt'].text())
        post_etiquetado = self.POS_ETI_DAO.buscar_categoria_id(
            id_post_etiquetado)
        if post_etiquetado:

            self.ventana.w3['id_pos_post_etiqueta_ipt'].setText(
                str(post_etiquetado[1]))

            self.ventana.w3['id_eti_post_etiqueta_ipt'].setText(
                str(post_etiquetado[2]))

    def handler_insertar_usuario(self):
        login = self.ventana.w3['login_usuario_ipt'].text()
        password = self.ventana.w3['password_usuario_ipt'].text()
        nickname = self.ventana.w3['nickname_usuario_ipt'].text()
        email = self.ventana.w3['email_usuario_ipt'].text()
        nuevo_id = self.crear_nuevo_id(self.USU_DAO.leer_categoria())
        nuevo_usuario = usuariosVO.UsuariosVO(
            id=nuevo_id, login=login, password=password, nickname=nickname, email=email)
        if self.USU_DAO.insertar_categoria(nuevo_usuario):
            print("Usuario insertado con éxito.")
            self.handler_leer_usuarios()

    def handler_leer_usuarios(self):
        usuarios = self.USU_DAO.leer_categoria()
        self.ventana.w3['tabla_usuario'].setRowCount(0)
        for usuario in usuarios:
            row = self.ventana.w3['tabla_usuario'].rowCount()
            self.ventana.w3['tabla_usuario'].insertRow(row)
            self.ventana.w3['tabla_usuario'].setItem(
                row, 0, QTableWidgetItem(str(usuario["id"])))
            self.ventana.w3['tabla_usuario'].setItem(
                row, 1, QTableWidgetItem(usuario["login"]))
            self.ventana.w3['tabla_usuario'].setItem(
                row, 2, QTableWidgetItem(usuario["password"]))
            self.ventana.w3['tabla_usuario'].setItem(
                row, 3, QTableWidgetItem(usuario["nickname"]))
            self.ventana.w3['tabla_usuario'].setItem(
                row, 4, QTableWidgetItem(usuario["email"]))

    def handler_actualizar_usuario(self):
        id_usuario = int(self.ventana.w3['buscar_id_usuario_ipt'].text())
        login = self.ventana.w3['login_usuario_ipt'].text()
        password = self.ventana.w3['password_usuario_ipt'].text()
        nickname = self.ventana.w3['nickname_usuario_ipt'].text()
        email = self.ventana.w3['email_usuario_ipt'].text()
        usuario_actualizado = usuariosVO.UsuariosVO(
            id=id_usuario, login=login, password=password, nickname=nickname, email=email)
        if self.USU_DAO.actualizar_categoria(usuario_actualizado):
            print("Usuario actualizado con éxito.")
            self.handler_leer_usuarios()

    def handler_eliminar_usuario(self):
        id_usuario = int(self.ventana.w3['buscar_id_usuario_ipt'].text())
        if self.USU_DAO.eliminar_categoria(id_usuario):
            print("Usuario eliminado con éxito.")
            self.handler_leer_usuarios()

    def handler_buscar_usuario(self):
        id_usuario = int(self.ventana.w3['buscar_id_usuario_ipt'].text())
        usuario = self.USU_DAO.buscar_categoria_id(id_usuario)
        if usuario:

            self.ventana.w3['login_usuario_ipt'].setText(usuario[1])
            self.ventana.w3['password_usuario_ipt'].setText(usuario[2])
            self.ventana.w3['nickname_usuario_ipt'].setText(usuario[3])
            self.ventana.w3['email_usuario_ipt'].setText(usuario[4])

    def crear_nuevo_id(self, lista):
        if lista:
            return max(item["id"] for item in lista) + 1
        return 1

    def mainloop(self):
        self.ventana.show()
        self.app.exec_()
