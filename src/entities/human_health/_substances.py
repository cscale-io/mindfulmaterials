from pydantic import BaseModel
from typing import Literal, Any

###########################################
# FACTORS
###########################################

class ReportingThreshold(BaseModel):
   value: Any

class ThirdPartyVerification(BaseModel):
   value: Any

class ExtentOfDisclosedInventory(BaseModel):
   value: Any

class Screening(BaseModel):
   value: Any

class Characterization(BaseModel):
   value: Any

class Identification(BaseModel):
   value: Any

class ClassBasedSubstanceAvoidance(BaseModel):
   value: Any

class AssessmentBasedOptimization(BaseModel):
   value: Any

class RestrictedSubstanceListScreening(BaseModel):
   value: Any

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