from modelo.VO.etiquetasVO import EtiquetasVO
from conexiondb import conectar_cliente


class CategoriasDAO:
    def __init__(self):
        self.cliente = conectar_cliente()
        self.coleccion = self.cliente.BlocDB.etiquetas

    def insertar_categoria(self, etiqueta: EtiquetasVO) -> bool:
        documento = {
            "id": etiqueta.id,
            "nombre_etiqueta": etiqueta.nombre_etiqueta
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
        etiqueta = self.coleccion.find()

        for row in etiqueta:
            lista.append(row)

        return lista

    def buscar_categoria_id(self, id):
        lista = []
        try:
            etiqueta = self.coleccion.find_one({"id": id})
            lista.append(etiqueta["id"])
            lista.append(etiqueta["nombre_etiqueta"])
        except:
            print("Error al encontrar el usuario")

        return lista

    def actualizar_categoria(self, etiqueta: EtiquetasVO):
        documento = {
            "$set": {
                "nombre_etiqueta": etiqueta.nombre_etiqueta
            }
        }
        try:
            self.coleccion.update_one({"id": etiqueta.id},
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
