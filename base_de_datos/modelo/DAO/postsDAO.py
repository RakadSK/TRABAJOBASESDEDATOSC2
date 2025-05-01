from modelo.VO.postsVO import PostsVO
from conexiondb import conectar_cliente


class PostsDAO:
    def __init__(self):
        self.cliente = conectar_cliente()
        self.coleccion = self.cliente.BlocDB.posts

    def insertar_categoria(self, post: PostsVO) -> bool:
        documento = {
            "id": post.id,
            "titulo": post.titulo,
            "fecha_publicacion": post.fecha_publicacion,
            "contenido": post.contenido,
            "estatus": post.estatus,
            "usuarios_id": post.usuario_id,
            "categoria_id": post.categoria_id
        }
        try:
            self.coleccion.insert_one(
                documento)
            return True
        except:
            print("Error al insertar Categoria")
            return False

    def leer_categoria(self):
        lista = []
        post = self.coleccion.find()

        for row in post:
            lista.append(row)

        return lista

    def buscar_categoria_id(self, id):
        lista = []
        try:
            post = self.coleccion.find_one({"id": id})
            lista.append(post["id"])
            lista.append(post["titulo"])
            lista.append(post["fecha_publicacion"])
            lista.append(post["contenido"])
            lista.append(post["estatus"])
            lista.append(post["usuario_id"])
            lista.append(post["categoria_id"])
        except:
            print("Error al encontrar el usuario")

        return lista

    def actualizar_categoria(self, post: PostsVO):
        documento = {
            "$set": {
                "titulo": post.titulo,
                "fecha_publicacion": post.fecha_publicacion,
                "contenido": post.contenido,
                "estatus": post.estatus,
                "usuarios_id": post.usuario_id,
                "categoria_id": post.categoria_id
            }
        }
        try:
            self.coleccion.update_one({"id": post.id},
                                      documento)
            return True
        except Exception as e:
            print("Error al insertar Categoria", e)
            return False

    def eliminar_categoria(self, id: int):
        try:
            self.coleccion.delete_one({"id": id})
            return True
        except Exception as e:
            print("Error al eliminar", e)
            return False
