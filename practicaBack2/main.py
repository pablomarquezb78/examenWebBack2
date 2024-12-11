from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import event_route, log_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto según el puerto de tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

app.include_router(event_route.router,prefix='/eventos')
app.include_router(log_route.router,prefix='/logs')