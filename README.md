# BTG-BACKEND-TEST Backend para Gestión de Fondos
## PRUEBA TÉCNICA PARA INGENIERO DE DESARROLLO 
### Parte 1: Fondos  (80%)

Este proyecto es una API RESTful desarrollada con **FastAPI** para la gestión de fondos de inversión. Permite a los usuarios realizar suscripciones, cancelar suscripciones, ver el historial de transacciones y recibir notificaciones por correo electrónico o SMS.

## Tabla de Contenidos

1. [Descripción](#descripción)
2. [Funcionalidades](#funcionalidades)
3. [Requisitos](#requisitos)
4. [Instalación y Ejecución](#instalación-y-ejecución)
   - [Ejecución con Docker](#ejecución-con-docker)
   - [Ejecución Local](#ejecución-local)
5. [Documentación Swagger](#documentación-swagger)
6. [Estructura del Proyecto](#estructura-del-proyecto)
7. [Pruebas](#pruebas)


## Descripción

La API permite a los usuarios gestionar sus fondos de inversión, donde pueden suscribirse a nuevos fondos, cancelar suscripciones existentes y consultar su historial de transacciones. Además, la API está integrada con un servicio de notificaciones que permite al usuario recibir alertas por SMS o correo electrónico.

## Funcionalidades

- **Suscribirse a Fondos**: Los usuarios pueden suscribirse a diferentes fondos de inversión.
- **Cancelar Suscripción**: Los usuarios pueden cancelar su suscripción a un fondo y recibir un reembolso del saldo asociado.
- **Historial de Transacciones**: Los usuarios pueden consultar las transacciones que han realizado (suscripciones y cancelaciones).
- **Notificaciones**: El usuario puede recibir notificaciones sobre sus transacciones por SMS o correo electrónico.

## Requisitos

Asegúrate de tener instalados los siguientes elementos:

- **Docker** y **Docker Compose** para la ejecución con contenedores.
- **Python 3.7+** si decides ejecutar la aplicación sin Docker.
- Una cuenta de **Twilio** para el envío de notificaciones SMS (opcional).

## Instalación y Ejecución

### Ejecución con Docker

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/cesarmauriciodr/BTG-BACKEND-TEST
   cd BTG-BACKEND-TEST
   ```

2. Construir y ejecutar los contenedores con Docker Compose:

   ```bash
   docker-compose up --build
   ```

   Esto levantará dos servicios:
   - **FastAPI** en `http://localhost:8000`
   - **MongoDB** en `localhost:27017` para almacenar los datos.

3. Verificar que la API esté funcionando visitando:

   ```
   http://localhost:8000
   ```

4. Para detener los contenedores:

   ```bash
   docker-compose stop
   ```

### Ejecución Local

Si prefieres no usar Docker, puedes ejecutar la aplicación localmente siguiendo estos pasos:

1. Crear un entorno virtual y activarlo:

   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

2. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación:

   ```bash
   cd app
   uvicorn app.main:app --reload
   ```

   La API estará disponible en `http://localhost:8000`.

## Documentación Swagger

FastAPI genera automáticamente una documentación interactiva **Swagger** para que puedas probar la API. Puedes acceder a ella en:

```
http://localhost:8000/docs
```

Además, puedes consultar la documentación en formato **ReDoc** en:

```
http://localhost:8000/redoc
```

Adicionalmente hay una copia de la documentacion en formato pdf

[https://github.com/cesarmauriciodr/BTG-BACKEND-TEST/blob/main/docs/api-docs.pdf]


## Estructura del Proyecto

```plaintext

 app/                         # Carpeta principal de la aplicación
│   ├── __init__.py              # Inicialización del paquete
│   ├── app.py                  # Punto de entrada de la aplicación (API FastAPI)
│   ├── models.py                # Modelos de datos (Pydantic)
│   ├── database.py              # Configuración de conexión con MongoDB
│   ├── notification.py          # Lógica para enviar notificaciones (SMS/Email)
│   └── routes/                  # Carpeta para organizar rutas
│       ├── __init__.py          # Inicialización del paquete de rutas
│       ├── subscriptions.py     # Rutas para gestionar suscripciones/cancelaciones
│       └── transactions.py      # Rutas para el historial de transacciones
│
├── data/                        # Carpeta para almacenar datos persistentes de MongoDB
│   └── mongo/                   # Datos persistentes de MongoDB (volumen de Docker)
│
├── Dockerfile                   # Archivo Docker para crear la imagen
├── docker-compose.yml           # Definición de servicios Docker
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Documentación del proyecto
└── tests/                       # Carpeta para pruebas unitarias
    ├── __init__.py              # Inicialización del paquete de pruebas
    ├── test_subscriptions.py    # Pruebas para la funcionalidad de suscripción/cancelación
    └── test_transactions.py     # Pruebas para el historial de transacciones
```

## Pruebas

El proyecto incluye pruebas unitarias

### Ejecución de pruebas


1. Ejecutar las pruebas:

   ```bash
   pytest
   ```

   Esto ejecutará todas las pruebas en la carpeta `tests/`.


### Parte 2: Consultas SQL (20%)

Solucion:

```sql
SELECT c.nombre, c.apellidos
FROM Cliente c
JOIN Inscripción i ON c.id = i.idCliente
JOIN Disponibilidad d ON i.idProducto = d.idProducto
JOIN Visitan v ON c.id = v.idCliente AND d.idSucursal = v.idSucursal;
```
