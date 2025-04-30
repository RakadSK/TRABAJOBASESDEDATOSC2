from dataclasses import dataclass
from typing import Optional


@dataclass
class UsuariosVO:
    id: Optional[int] = None
    login: Optional[str] = None
    password: Optional[str] = None
    nickname: Optional[str] = None
    email: Optional[str] = None
