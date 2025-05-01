from modelo.VO.categoriasVO import CategoriasVO
from conexiondb import conectar_cliente


class CategoriasDAO:
    def __init__(self):
        self.cliente = conectar_cliente()
        self.coleccion = self.cliente.BlocDB.categorias

    def insertar_categoria(self, categoria: CategoriasVO) -> bool:
        documento = {
            "id": categoria.id,
            "nombre_categoria": categoria.nombre_categoria
        }
        try:
            self.coleccion.insert_one(
                documento)
            return True
        except:
            print("Error al Insertar Categoria")
            return False

    def leer_categoria(self):
        lista = []
        categoria = self.coleccion.find()

        for row in categoria:
            lista.append(row)
        
        print("categorias: ", lista)

        return lista

    def buscar_categoria_id(self, id):
        lista = []
        categoria = self.coleccion.find_one({"id": id})
        lista.append(categoria["id"])
        lista.append(categoria["nombre_categoria"])

        return lista

    def actualizar_categoria(self, categoria: CategoriasVO):
        documento = {
            "$set": {
                "nombre_categoria": categoria.nombre_categoria
            }
        }
        try:
            self.coleccion.update_one({"id": categoria.id},
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


dao = CategoriasDAO()
dao.leer_categoria()


# NOTA IMPORTANTE PARA MANJEAR LOS LEER
#  for categoria in lista:
# print(categoria["id"], categoria["nombre_categoria"])

# NOTA IMPORTANTE PARA ACTUALIZAR/ELIMINAR
# dao.actualizar_categoria(categoria=CategoriasVO(
# id=2, nombre_categoria="Papas"))
