from dataclasses import dataclass

@dataclass
class Usuario:
    """
    Representa la entidad Usuario en el sistema.
    Separar el modelo permite que todas las capas hablen el mismo idioma.
    """
    username: str
    password: str  # En la práctica, aquí viajaría el hash o el texto plano según el flujo