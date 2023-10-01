import uvicorn
from fastapi import FastAPI

from src.core import config
from src.api.base import router

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json'
)

app.include_router(router, prefix='/api')

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=config.PROJECT_HOST,
        port=config.PROJECT_PORT,
    )
