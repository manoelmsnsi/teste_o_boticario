import os
import elasticapm
from fastapi import  FastAPI,Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from elasticapm.contrib.starlette import ElasticAPM, make_apm_client



from src.app.auth.route import backend as backend_auth
from src.app.compra.route import backend as backend_compra
from src.app.cashback.route import backend as backend_cashback
from src.app.revendedor.route import backend as backend_revendedor

app = FastAPI(
    title="O BOTICARIO",
    description="<a href='https://www.linkedin.com/in/manoel-messias-731659121/' target='__blank'>Manoel Messias da Silva Neto</a><br>",
    version="0.1.0",
    
)


# Configurar o CORS
origins = [
    "*",  
]
# Configure o Elastic APM
ELASTIC_APM_CONFIG = { 
    'SERVICE_NAME': os.environ.get("ELASTIC_SERVICE_NAME", "o-boticario-service"),  # Nome do serviço
    'SECRET_TOKEN': os.environ.get("ELASTIC_SECRET_TOKEN", ''),  # Se necessário
    'SERVER_URL': os.environ.get("ELASTIC_SERVER_URL","http://apm-server:8200"),  # URL do seu servidor APM
    'SERVER_USER': os.environ.get("ELASTIC_USER", "elastic"),
    'SERVER_PASSWORD': os.environ.get("ELASTIC_PASSWORD", "changeme"),
    'TIMEOUT': 15  # Tempo limite de 15 segundos
}
ELASTIC_APM = make_apm_client(ELASTIC_APM_CONFIG)
app.add_middleware(ElasticAPM, client=ELASTIC_APM)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",tags=["HOME"])
async def get_home():  
    return {"-- API--"}

app.include_router(backend_auth)
app.include_router(backend_revendedor)
app.include_router(backend_compra)
app.include_router(backend_cashback)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    elasticapm.label(detail=str(exc.__dict__))
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status_code": exc.status_code,
            "detail": exc.detail,
        },
    )

# Custom exception handler for RequestValidationError
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    elasticapm.label(detail=str(exc.__dict__))
    return JSONResponse(
        status_code=422,
        content={
            "status_code": 422,
            "detail": str(exc.errors()),
        },
    )

# Custom exception handler for general exceptions
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    elasticapm.get_client().capture_exception()
    return JSONResponse(
        status_code=500,
        content={
            "status_code": 500,
            "detail": str(exc),
        },
    )
