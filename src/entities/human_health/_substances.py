from pydantic import BaseModel, Field
from typing import Any, Optional, List
from enum import Enum
from ..utilties import field_descriptions

###########################################
# FACTORS
###########################################

_factor_descriptions = {
  "ReportingThreshold": "1.1.1.1 Reporting Threshold Level",
  "ThirdPartyVerification": "1.1.1.2 Third-Party Verified",
  "ExtentOfDisclosedInventory": "1.1.1.3 Extent of Disclosed Inventory",
  "Screening": "1.1.1.4 Screened",
  "Characterization": "1.1.1.5 Characterized",
  "Identification": "1.1.1.6 Identified",
  "ClassBasedSubstanceAvoidance": "1.1.4.1 Class-Based Substance Avoidance",
  "AssessmentBasedOptimization": "1.1.4.2 Assessment-Based Optimization.",
  "RestrictedSubstanceListScreening": "1.1.4.3 Restricted Substance List (RSL) Screening Compliance"
}

# Reporting Threshold

class ReportingThresholdMetric(Enum):
    PPM_100 = "100 ppm"
    PPM_1000 = "1,000 ppm" 
    PPM_10000 = "10,000 ppm"

class ReportingThreshold(BaseModel):
   metric: Optional[ReportingThresholdMetric] = Field(None, description=field_descriptions['metric'])
   description: str = Field(_factor_descriptions['ReportingThreshold'], 
                        description=field_descriptions['description'])

# Third-Party Verification

class ThirdPartyVerification(BaseModel):
    metric: Optional[bool] = Field(None, description=field_descriptions['metric'])
    description: str = Field(_factor_descriptions['ThirdPartyVerification'], 
                           description=field_descriptions['description'])
   #  standard: Any = Field(None, description=field_descriptions['standard'])

# Extent of Disclosed Inventory

class InventoryDisclosure(Enum):
   DISCLOSURE_100_PUBLIC = "100% publicly disclosed inventory"
   DISCLOSURE_99_PUBLIC = ">= 99% publicly disclosed inventory"
   DISCLOSURE_75_PUBLIC = ">= 75% publicly disclosed inventory"
   NOT_PUBLIC = "Inventory not public"
   DISCLOSURE_100_THIRD_PARTY = "Inventory not public, but 100% disclosed to 3rd party"

class ExtentOfDisclosedInventory(BaseModel):
   metric: Optional[InventoryDisclosure] = Field(None, description=field_descriptions['metric'])
   description: str = Field(_factor_descriptions['ReportingThreshold'], 
                        description=field_descriptions['description'])

# Screened?

class Screening(BaseModel):
   metric: Optional[bool] = Field(None, description=field_descriptions['metric'])
   description: str = Field(_factor_descriptions['Screening'], 
                          description=field_descriptions['description'])

# Characterized?

class Characterization(BaseModel):
   metric: Optional[bool] = Field(None, description=field_descriptions['metric'])
   description: str = Field(_factor_descriptions['Characterization'], 
                          description=field_descriptions['description'])

# Identified?

class Identification(BaseModel):
   metric: Optional[bool] = Field(None, description=field_descriptions['metric'])
   description: str = Field(_factor_descriptions['Identification'], 
                          description=field_descriptions['description'])

# Class-Based Substance Avoidance

class AvoidedSubstance(Enum):
   NO_ANTIMICROBIALS = "No Antimicrobials"
   NO_BISPHENOLS = "No Bisphenols"
   NO_FLAME_RETARDANTS = "No Flame Retardants"
   NO_FORMALDEHYDES = "No Formaldehydes"
   NO_ORTHO_PHTHALATES = "No Ortho-Phthalates"
   NO_PFAS = "No PFAS"
   NO_PVC_CPVC = "No Polyvinyl Chloride or Chlorinated Polyvinyl Chloride"
   NO_ALKYLPHENOLS = "No Alkylphenols"
   NO_CHLOROPHENOLS = "No Chlorophenols"
   NO_ISOCYANATES = "No Isocyanates"
   NO_METHYL_ACRYLATE = "No Methyl & Acrylate Groups"
   NO_TOXIC_METALS = "No Toxic Metals & Compounds"
   NO_STYRENE_BUTADIENE = "No Styrene Butadiene Rubber"
   NO_CRUMB_RUBBER = "No Crumb Rubber"
   NO_FLY_ASH = "No Fly Ash"
   NO_AZO_DYES = "No Azo Dyes"

# Class-Based Substance Avoidance

class ClassBasedSubstanceAvoidance(BaseModel):
   metric: Optional[List[AvoidedSubstance]] = Field(None, description=field_descriptions['metric'])
   description: str = Field(_factor_descriptions['ClassBasedSubstanceAvoidance'], 
                           description=field_descriptions['description'])

# Assessment-Based Optimization

class OptimizationPercentage(Enum):
   HUNDRED_PERCENT = "100%"
   NINETY_FIVE_PERCENT = "95%"
   SEVENTY_FIVE_PERCENT = "75%"

class AssessmentBasedOptimization(BaseModel):
   metric: Optional[OptimizationPercentage] = Field(None, description=field_descriptions['metric'])
   description: str = Field(_factor_descriptions['AssessmentBasedOptimization'], 
                        description=field_descriptions['description'])

# Restricted Substance List (RSL) Screening Compliance

class RestrictedSubstanceList(Enum):
   GREENSCREEN_BM1_LT1 = "GreenScreen BM-1 or LT-1 Chemicals"
   REACH_SVHC = "REACH Candidate List of Substances of Very High Concern (SVHC)"
   LBC_RED_LIST_V4_APR2024 = "Living Building Challenge Red List Substances - v4.0 (April 2024 Update)"
   LBC_RED_LIST_V3_1 = "Living Building Challenge Red List Substances - v3.1"
   C2C_RESTRICTED_V4 = "Cradle to Cradle Restricted Substances (version 4)"
   C2C_BANNED_V3 = "Cradle to Cradle Banned List Substances (version 3)"
   SIN_LIST = "SIN List"
   GSPI_SIX_CLASSES = "Green Science Policy Institute Six Classes"
   PERKINS_WILL_PRECAUTIONARY = "Perkins+Will Precautionary List"
   KAISER_EPP_CHEMICALS = "Kaiser Permanente EPP Chemicals of Concern"
   CA_EPA_PROP65 = "CA EPA - Prop 65"
   EPA_PRIORITY_PBTS = "US EPA - Priority PBTs (PPT)"
   EPA_TRI_PBTS = "US EPA - Toxics Release Inventory PBTs"
   LBC_RED_LIST_V4_MAR2022 = "Living Building Challenge Red List Substances - v4.0 (March 2022 Update)"
   HCWH_HEALTHY_INTERIORS = "HCWH Healthy Interiors: Furniture & Furnishings, v2.4"
   REACH_AUTHORIZATION = "REACH Authorization List (Annex XIV)"
   REACH_RESTRICTIONS = "REACH Restrictions List (Annex XVII)"
   LBC_RED_LIST_V4_APR2023 = "Living Building Challenge Red List Substances - v4.0 (April 2023 Update)"
   ROHS_RESTRICTED = "RoHS Restricted Substances, EU (ANNEX II, Version 2.0)"

class RestrictedSubstanceListScreening(BaseModel):
   metric: Optional[List[RestrictedSubstanceList]] = Field(None, description=field_descriptions['metric'])
   description: str = Field(_factor_descriptions['RestrictedSubstanceListScreening'], 
                          description=field_descriptions['description'])

###########################################
# CATEGORIES
###########################################

class Transparency(BaseModel):
   reporting_threshold: ReportingThreshold
   third_party_verification: ThirdPartyVerification
   extent_of_disclosed_inventory: ExtentOfDisclosedInventory
   screening: Screening
   characterization: Characterization
   identification: Identification

class Optimization(BaseModel):
   class_based_substance_avoidance: ClassBasedSubstanceAvoidance
   assessment_based_optimization: AssessmentBasedOptimization
   restricted_substance_list_screening: RestrictedSubstanceListScreening

###########################################
# SUB-BUCKET
###########################################

class Substances(BaseModel):
   transparency: Transparency
   optimization: Optimization