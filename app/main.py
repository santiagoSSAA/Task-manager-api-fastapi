from fastapi import FastAPI
from app.api.endpoints import tasks
from app.db.database import engine
from app.models import task

app = FastAPI(title="API de Gestión de Tareas")

# Crear tablas en la base de datos
task.Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(tasks.router)

