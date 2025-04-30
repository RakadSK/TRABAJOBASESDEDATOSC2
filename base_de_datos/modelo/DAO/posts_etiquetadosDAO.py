from modelo.VO.posts_etiquetadosVO import PostEtiquetadosVO
from conexiondb import conectar_cliente


class CategoriasDAO:
    def __init__(self):
        self.cliente = conectar_cliente()
        self.coleccion = self.cliente.BlocDB.posts_etiquetados

    def insertar_categoria(self, post_etiquetado: PostEtiquetadosVO) -> bool:
        documento = {
            "id": post_etiquetado.id,
            "post_id": post_etiquetado.post_id,
            "etiqueta_id": post_etiquetado.etiqueta_id
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
        post_etiquetado = self.coleccion.find()

        for row in post_etiquetado:
            lista.append(row)

        return lista

    def buscar_categoria_id(self, id):
        lista = []
        try:
            post_etiquetado = self.coleccion.find_one({"id": id})
            lista.append(post_etiquetado["id"])
            lista.append(post_etiquetado["post_id"])
            lista.append(post_etiquetado["etiqueta_id"])
        except:
            print("Error al encontrar el usuario")

        return lista

    def actualizar_categoria(self, post_etiquetado: PostEtiquetadosVO):
        documento = {
            "$set": {
                "post_id": post_etiquetado.post_id,
                "etiqueta.id": post_etiquetado.etiqueta_id
            }
        }
        try:
            self.coleccion.update_one({"id": post_etiquetado.id},
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
