from pydantic import BaseModel
from typing import Literal, Any

###########################################
# FACTORS
###########################################

class ApplicableVOCTesting(BaseModel):
   value: Any

class VOCContentRegulatory(BaseModel):
   value: Any

class VOCContentStandardCompliance(BaseModel):
   value: Any

class VOCContentSCAQMDCompliance(BaseModel):
   value: Any

class VOCEmissionsCompliance(BaseModel):
   value: Any

class TVOCEmissionsRange(BaseModel):
   value: Any

class EmissionsModelingScenario(BaseModel):
   value: Any

class CompositeWoodFormaldehydeCompliance(BaseModel):
   value: Any

class FurnitureBIFMACompliance(BaseModel):
   value: Any

###########################################
# CATEGORIES
###########################################

class Assessment(BaseModel):
   applicable_voc_testing: ApplicableVOCTesting
   voc_content_regulatory: VOCContentRegulatory

class Optimization(BaseModel):
   voc_content_standard_compliance: VOCContentStandardCompliance
   voc_content_scaqmd_compliance: VOCContentSCAQMDCompliance
   voc_emissions_compliance: VOCEmissionsCompliance
   tvoc_emissions_range: TVOCEmissionsRange
   emissions_modeling_scenario: EmissionsModelingScenario
   composite_wood_formaldehyde_compliance: CompositeWoodFormaldehydeCompliance
   furniture_bifma_compliance: FurnitureBIFMACompliance

###########################################
# SUB-BUCKET
###########################################

class VOCs(BaseModel):
   assessment: Assessment
   optimization: Optimization