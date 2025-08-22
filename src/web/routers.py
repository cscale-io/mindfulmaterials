from fastapi import APIRouter
from src.entities.common_material_framework import CommonMaterialsSchema
from src.services.validation import validate_data

schema_router = APIRouter(prefix="/schema", tags=["Data Checking"])

@schema_router.post(
   "/check", 
   response_model=CommonMaterialsSchema,
   description=(
       "Check your data against the Common Materials Schema. "
       "Use this endpoint to check that your input data is properly formatted "
       "and aligns with the CMF structure before submitting or storing it."
   )
)
async def check_your_data(data: CommonMaterialsSchema) -> CommonMaterialsSchema:
   return await validate_data(data)