# API de Gestión de Tareas

Esta es una API simple para gestionar tareas, construida con FastAPI y SQLite. Permite crear, obtener y eliminar tareas.

## Requisitos

- Python 3.11 o superior
- FastAPI
- SQLite
- pytest (para pruebas)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tuusuario/tarea-api.git
   cd tarea-api
   ```

2. Crea un entorno virtual y actívalo:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

```
tarea-api/
│
├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── crud/
│   ├── api/
│   │   └── endpoints/
│   └── db/
│
├── tests/
│   └── test_api/
│
├── README.md
├── requirements.txt
├──docker-compose.yml
└── ARCHITECTURE.md
```

- `app/`: Contiene el código principal de la aplicación.
- `tests/`: Contiene las pruebas unitarias y de integración.
- `README.md`: Este archivo, con instrucciones y documentación.
- `requirements.txt`: Lista de dependencias del proyecto.
- `docker-compose.yml`: Configuración de Docker para el proyecto.
- `ARCHITECTURE.md`: Descripción de los patrones de arquitectura y diseño utilizados en el proyecto.


## Ejecución de la API

Para ejecutar la API en modo de desarrollo:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://localhost:8000`.

## Uso de la API

### Crear una tarea

```bash
curl -X POST "http://localhost:8000/tasks/" -H "Content-Type: application/json" -d '{"title":"Nueva Tarea","description":"Descripción de la tarea"}'
```

### Obtener todas las tareas

```bash
curl "http://localhost:8000/tasks/"
```

### Eliminar una tarea

```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

## Documentación de la API

FastAPI genera automáticamente la documentación de la API. Puedes acceder a ella en:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Ejecución de Pruebas

Para ejecutar las pruebas:

```bash
pytest
```

## Uso con Docker

Si prefieres usar Docker:

1. Asegúrate de tener Docker y Docker Compose instalados.

2. Construye y ejecuta los contenedores:

   ```bash
   docker-compose up --build
   ```

La API estará disponible en `http://localhost:8000`.


## Habilidades evaluadas


| **Categoría**          | **Tecnología/Habilidad**                      | **Descripción**                                             |
|-----------------------|----------------------------------------------|-----------------------------------------------------------|
| **Lenguajes de Programación** | Python                                       | Dominio del lenguaje Python y su ecosistema.               |
| **Frameworks**        | FastAPI                                      | Desarrollo de APIs RESTful y asincrónicas.                |
|                       | Flask/Django                                 | Alternativas para construir APIs si es necesario.         |
| **Contenerización**   | Docker                                       | Creación y gestión de contenedores.                        |
|                       | Kubernetes                                   | Orquestación de contenedores en la nube.                  |
| **Bases de Datos**    | SQLite                              | Gestión y optimización de bases de datos.                  |
| **Colas de Mensajes** | Kafka                             | Integración y manejo de sistemas de mensajería.           |
| **Desarrollo Ágil**   | CI/CD                                        | Implementación de pipelines de integración y despliegue continuo. |
| **Programación Asincrónica** | asyncio, aiohttp                         | Experiencia en programación asincrónica y arquitecturas impulsadas por eventos. |
| **Pruebas**           | pytest                             | Desarrollo y mantenimiento de pruebas unitarias e integradas. |
| **Mejores Prácticas** | Patrones de Diseño                           | Adherencia a prácticas y patrones de diseño en Python.     |
|                       | Código Limpio y Mantenible                  | Enfoque en la calidad del código y su mantenibilidad.      |

## Descripción del proyecto

Aquí tienes un ejemplo de ejercicio que puede evaluar las habilidades necesarias para el rol de **Senior Python Backend Developer**, y que debería tomarse alrededor de 30 minutos:

### Ejercicio: API de Gestión de Tareas

**Objetivo:** Crear una API simple para gestionar tareas utilizando FastAPI, con operaciones para crear, obtener y eliminar tareas. La API debe integrarse con una base de datos SQLite para almacenamiento.

#### Requisitos:

1. **Endpoints:**
- `POST /tasks`: Crear una nueva tarea (requiere un JSON con `title` y `description`).
- `GET /tasks`: Obtener la lista de todas las tareas.
- `DELETE /tasks/{task_id}`: Eliminar una tarea específica por su ID.

2. **Base de Datos:**
- Utilizar SQLite para almacenar las tareas.
- Definir un modelo de datos para las tareas, que incluya `id`, `title`, y `description`.

3. **Validación:**
- Validar que el título no esté vacío al crear una tarea.

4. **Pruebas:**
- Incluir al menos una prueba unitaria que valide la creación de una tarea.

#### Entregables:

- Código fuente en un repositorio de Git (por ejemplo, GitHub).
- Un archivo README que explique cómo ejecutar la API y cómo correr las pruebas.

#### Consideraciones:

- Utilizar `pytest` para las pruebas.
- Asegurarse de que el código siga las mejores prácticas de Python y FastAPI.
- Incluir comentarios que expliquen las partes clave del código.


## Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de crear un pull request.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)