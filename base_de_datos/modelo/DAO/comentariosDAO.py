from modelo.VO.comentariosVO import ComentariosVO
from conexiondb import conectar_cliente


class CategoriasDAO:
    def __init__(self):
        self.cliente = conectar_cliente()
        self.coleccion = self.cliente.BlocDB.comentarios

    def insertar_categoria(self, comentario: ComentariosVO) -> bool:
        documento = {
            "id": comentario.id,
            "cuerpo_comentario": comentario.cuerpo_comentario,
            "usuario_id": comentario.usuario_id,
            "post_id": comentario.post_id
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
        comentario = self.coleccion.find()

        for row in comentario:
            lista.append(row)

        return lista

    def buscar_categoria_id(self, id):
        lista = []
        try:
            comentario = self.coleccion.find_one({"id": id})
            lista.append(comentario["id"])
            lista.append(comentario["cuerpo_comentario"])
            lista.append(comentario["usuario_id"])
            lista.append(comentario['post_id'])
        except:
            print("Error al encontrar el usuario")

        return lista

    def actualizar_categoria(self, comentario: ComentariosVO):
        documento = {
            "$set": {
                "cuerpo_comentario": comentario.cuerpo_comentario,
                "usuario_id": comentario.usuario_id,
                "post_id": comentario.post_id
            }
        }
        try:
            self.coleccion.update_one({"id": comentario.id},
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
