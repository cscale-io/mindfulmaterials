from pydantic import BaseModel, Field
from typing import Any, Optional, List
from enum import Enum
from ..utilties import field_descriptions

###########################################
# FACTORS
###########################################

_factor_descriptions = {
   "ApplicableVOCTesting": "1.2.2.1 Applicable VOC Testing",
   "VOCContentRegulatory": "1.2.2.2 VOC Content (Regulatory) (g/L)",
   "VOCContentCarb2007": "1.2.4.1 VOC Content - CARB 2007 Compliance",
   "VOCContentSCAQMDCompliance": "1.2.4.2 VOC Content - SCAQMD Compliance Level",
   "VOCEmissionsCompliance": "1.2.4.3 VOC Emissions Compliance",
   "TVOCEmissionsRange": "1.2.4.4 TVOC Emissions Range",
   "EmissionsModelingScenario": "1.2.4.5 Emissions Modeling Scenario for Compliance",
   "CompositeWoodFormaldehydeCompliance": "1.2.4.6 Composite Wood - Formaldehyde Emissions Compliance (CARB & TSCA Title VI)",
   "FurnitureBIFMACompliance": "1.2.4.7 Furniture - ANSI/BIFMA M7.1-2011 Compliance"
   }

# Applicable VOC Testing

class VOCTestingType(Enum):
   VOC_CONTENT = "VOC Content"
   VOC_EMISSIONS = "VOC Emissions"
   FORMALDEHYDE_EMISSIONS = "Formaldehyde Emissions"
   INHERENTLY_NON_EMITTING = "Inherently Non-Emitting"

class ApplicableVOCTesting(BaseModel):
   metric: Optional[List[VOCTestingType]] = Field(None, description=field_descriptions['metric'])
   description: str = _factor_descriptions['ApplicableVOCTesting']
   standard: Any = Field(None, description=field_descriptions['standard'])

# VOC Content (Regulatory)

class VOCContentRegulatory(BaseModel):
    metric: Optional[float] = Field(None, ge=0, le=1000, description=field_descriptions['metric'])
    description: str = _factor_descriptions['VOCContentRegulatory']
    standard: Any = Field(None, description=field_descriptions['standard'])

# VOC Content (CARB 2007)

class VOCContentCarb2007Compliance(BaseModel):
   metric: Optional[bool] = Field(None, description=field_descriptions['metric'])
   description: str = _factor_descriptions['VOCContentCarb2007']
   standard: Any = Field(None, description=field_descriptions['standard'])

# VOC Content - SCAQMD Compliance

class SCAQMDCompliance(Enum):
   NON_COMPLIANT = "Non-Compliant"
   ZERO_VOC = "Zero VOC"
   COMPLIANT = "Compliant (Low-VOC)"
   SUPER_COMPLIANT = "Super-Compliant"

class VOCContentSCAQMDCompliance(BaseModel):
   metric: Optional[SCAQMDCompliance] = Field(None, description=field_descriptions['metric'])
   description: str = _factor_descriptions['VOCContentSCAQMDCompliance']
   standard: Any = Field(None, description=field_descriptions['standard'])

# VOC Emissions Compliance

class VOCEmissionsStandard(Enum):
   INHERENTLY_NON_EMITTING = "Inherently Non-Emitting"
   CDPH_V1_1 = "CDPH Standard Method v1.1-2010"
   CDPH_V1_2 = "CDPH Standard Method v1.2-2017"
   GREEN_LABEL_PLUS = "Green Label Plus (GLP) Emissions Criteria v2.01-2017"

class VOCEmissionsCompliance(BaseModel):
   metric: Optional[VOCEmissionsStandard] = Field(None, description=field_descriptions['metric'])
   description: str = _factor_descriptions['VOCEmissionsCompliance']
   standard: Any = Field(None, description=field_descriptions['standard'])

# TVOC Emissions Range

class TVOCRange(Enum):
   UNDER_0_22 = "0.22 mg/m3 or less"
   UNDER_0_50 = "0.50 mg/m3 or less"
   BETWEEN_0_50_AND_5_00 = "0.50 to 5.00 mg/m3"
   OVER_5_00 = "5.00 mg/m3 or more"

class TVOCEmissionsRange(BaseModel):
   metric: Optional[TVOCRange] = Field(None, description=field_descriptions['metric'])
   description: str = _factor_descriptions['TVOCEmissionsRange']
   standard: Any = Field(None, description=field_descriptions['standard'])

# Emissions Modeling Scenario

class ModelingScenario(Enum):
   PRIVATE_OFFICE = "Private Office Scenario"
   SCHOOL_CLASSROOM = "School Classroom Scenario"
   SINGLE_FAMILY_RESIDENCE = "Single-Family Residence Scenario"
   OPEN_PLAN_OFFICE = "Open Plan Office Scenario"
   SEATING = "Seating Scenario"

class EmissionsModelingScenario(BaseModel):
   metric: Optional[List[ModelingScenario]] = Field(None, description=field_descriptions['metric'])
   description: str = _factor_descriptions['EmissionsModelingScenario']
   standard: Any = Field(None, description=field_descriptions['standard'])

# Composite Wood - Formaldehyde Emissions Compliance

class FormaldehydeCompliance(Enum):
   NO_ADDED_FORMALDEHYDE = "No Added Formaldehyde"
   ULTRA_LOW_EMITTING = "Ultra Low Emitting Formaldehyde"
   NOT_APPLICABLE = "Not Applicable"
   CARB_EXEMPT = "CARB Exempt"

class CompositeWoodFormaldehydeCompliance(BaseModel):
   metric: Optional[FormaldehydeCompliance] = Field(None, description=field_descriptions['metric'])
   description: str = _factor_descriptions['CompositeWoodFormaldehydeCompliance']
   standard: Any = Field(None, description=field_descriptions['standard'])

# Furniture - BIFMA Compliance

class BIFMASection(Enum):
    SECTION_7_6_1 = "Section 7.6.1"
    SECTION_7_6_2 = "Section 7.6.2" 
    SECTION_7_6_3 = "Section 7.6.3"

class FurnitureBIFMACompliance(BaseModel):
    metric: Optional[List[BIFMASection]] = Field(None, description=field_descriptions['metric'])
    description: str = _factor_descriptions['FurnitureBIFMACompliance']
    standard: Any = Field(None, description=field_descriptions['standard'])

###########################################
# CATEGORIES
###########################################

class Assessment(BaseModel):
   applicable_voc_testing: ApplicableVOCTesting
   voc_content_regulatory: VOCContentRegulatory

class Optimization(BaseModel):
   voc_content_carb2007_compliance: VOCContentCarb2007Compliance
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