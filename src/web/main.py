from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ValidationError

from fastapi import FastAPI
from src.web.routers import schema_router

app = FastAPI(docs_url="/swagger")

app.mount("/", StaticFiles(directory="public", html=True), name="static")
app.include_router(schema_router)


