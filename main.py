from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import map_route

app = FastAPI()

# Configuración del middleware CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Cambia esto según el puerto de tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

# Incluir las rutas
app.include_router(map_route.router, prefix='/mapas')