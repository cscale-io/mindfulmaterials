from src.entities.common_material_framework import CommonMaterialsSchema

async def validate_data(data: CommonMaterialsSchema) -> CommonMaterialsSchema:
    return data