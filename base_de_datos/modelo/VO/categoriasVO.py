from dataclasses import dataclass
from typing import Optional


@dataclass
class CategoriasVO:
    id: Optional[int] = None
    nombre_categoria: Optional[str] = None
