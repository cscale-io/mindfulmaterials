from fastapi import APIRouter
from src.entities.common_material_framework import CommonMaterialsSchema
from src.services.validation import validate_data

schema_router = APIRouter(prefix="/schema", tags=["schema"])

@schema_router.post("/validate", response_model=CommonMaterialsSchema)
async def validate_endpoint(data: CommonMaterialsSchema) -> CommonMaterialsSchema:
    return await validate_data(data)