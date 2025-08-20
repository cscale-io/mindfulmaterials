from pydantic import BaseModel
from typing import Optional

from .human_health.bucket import HumanHealth

###########################################
# PLACEHOLDERS
###########################################

class ProductData(BaseModel):
   pass  

class SocialHealthEquity(BaseModel):
   pass  

class EcosystemHealth(BaseModel):
   pass  

class ClimateHealth(BaseModel):
   pass  

class CircularEconomy(BaseModel):
   pass  

###########################################
# PARENT SCHEMA
###########################################

class CommonMaterialsSchema(BaseModel):
   product_data: Optional[ProductData] = None
   human_health: Optional[HumanHealth] = None
   social_health_equity: Optional[SocialHealthEquity] = None
   ecosystem_health: Optional[EcosystemHealth] = None
   climate_health: Optional[ClimateHealth] = None
   circular_economy: Optional[CircularEconomy] = None