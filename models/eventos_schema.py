from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone

class eventosSchema(BaseModel):
    nombre: str = Field(..., description="nombre del evento")
    timestamp: datetime = Field(..., description="fecha y hora de comienzo del evento")
    lugar: str = Field(..., description="direccion postal del evento")
    lat: float = Field(..., description="latitud coordenada gps")
    lon:float = Field(...,description="longitud coordenada gps")
    organizador: str = Field(..., description="email del creador del evento")
    imagen: str = Field(..., description="URI de una imagen promocional del evento")

    model_config = {
        "json_schema_extra" : {
            "example" : 
           {
            "nombre": "Conferencia de Tecnología",
            "timestamp": "2023-10-10T15:00:00",
            "lugar": "123 Calle Principal, Ciudad, País",
            "lat": 40.712776,
            "lon": -74.005974,
            "organizador": "organizador@example.com",
            "imagen": "http://example.com/imagen.jpg"
            }
        }
    }