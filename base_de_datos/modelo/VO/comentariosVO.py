from dataclasses import dataclass
from typing import Optional


@dataclass
class ComentariosVO:
    id: Optional[int] = None
    cuerpo_comentario: Optional[str] = None
    usuario_id: Optional[int] = None
    post_id: Optional[int] = None
