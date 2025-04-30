from dataclasses import dataclass
from typing import Optional


@dataclass
class EtiquetasVO:
    id: Optional[int] = None
    nombre_etiqueta: Optional[str] = None
