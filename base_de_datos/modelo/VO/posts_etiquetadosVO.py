from dataclasses import dataclass
from typing import Optional


@dataclass
class PostEtiquetadosVO:
    id: Optional[int] = None
    post_id: Optional[int] = None
    etiqueta_id: Optional[int] = None
