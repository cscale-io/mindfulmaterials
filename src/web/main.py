from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, ValidationError

from fastapi import FastAPI
from src.web.routers import schema_router

app = FastAPI(
   title="Common Materials Schema",
   version="BETA",
   description=(
       "A machine-readable implementation of the Common Materials Framework, "
       "developed by [C.Scale](https://cscale.io) to facilitate the easy "
       " exchange of product sustainability data across the building industry."
   ),
   contact={
       "name": "Mindful Materials",
       "url": "https://mindfulmaterials.com"
   },
   docs_url="/swagger"
)

app.mount("/", StaticFiles(directory="public", html=True), name="static")
app.include_router(schema_router)


