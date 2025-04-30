from dataclasses import dataclass
from typing import Optional


@dataclass
class PostsVO:
    id: Optional[int] = None
    titulo: Optional[str] = None
    fecha_publicacion: Optional[str] = None
    contenido: Optional[str] = None
    estatus: Optional[str] = None
    usuario_id: Optional[int] = None
    categoria_id: Optional[int]
