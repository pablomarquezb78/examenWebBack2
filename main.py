from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from routes import event_route, log_route

app = FastAPI()

# Middleware para redirigir HTTP a HTTPS
app.add_middleware(HTTPSRedirectMiddleware)

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
app.include_router(event_route.router, prefix='/eventos')
app.include_router(log_route.router, prefix='/logs')
