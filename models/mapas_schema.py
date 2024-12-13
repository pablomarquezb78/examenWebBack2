from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone
from typing import List

class Coordinate(BaseModel):
    lat: float
    lon: float
    nombre: str
    imagen: str

class mapasSchema(BaseModel):
    email: str = Field(..., description="email del usuario")
    marcadores: List[Coordinate] = Field(..., description="Lista de coordenadas de visitas del usuario")

    model_config = {
        "json_schema_extra" : {
            "example" : 
           {
                "email": "usuario@example.com",
                "marcadores": [
                    {"latitud": 40.712776, "longitud": -74.005974},
                    {"latitud": 34.052235, "longitud": -118.243683}
                ]
            }
        }
    }