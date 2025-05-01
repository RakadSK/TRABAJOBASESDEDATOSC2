from modelo.VO.usuariosVO import UsuariosVO
from conexiondb import conectar_cliente


class UsuariosDAO:
    def __init__(self):
        self.cliente = conectar_cliente()
        self.coleccion = self.cliente.BlocDB.usuarios

    def insertar_categoria(self, usuario: UsuariosVO) -> bool:
        documento = {
            "id": usuario.id,
            "login": usuario.login,
            "password": usuario.password,
            "nickname": usuario.nickname,
            "email": usuario.email
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
        usuario = self.coleccion.find()

        for row in usuario:
            lista.append(row)

        return lista

    def buscar_categoria_id(self, id):
        lista = []
        try:
            usuario = self.coleccion.find_one({"id": id})
            lista.append(usuario["id"])
            lista.append(usuario["login"])
            lista.append(usuario["password"])
            lista.append(usuario["nickname"])
            lista.append(usuario["email"])
        except:
            print("Error al encontrar el usuario")

        return lista

    def actualizar_categoria(self, usuario: UsuariosVO):
        documento = {
            "$set": {
                "login": usuario.login,
                "password": usuario.password,
                "nickname": usuario.nickname,
                "email": usuario.email
            }
        }
        try:
            self.coleccion.update_one({"id": usuario.id},
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
