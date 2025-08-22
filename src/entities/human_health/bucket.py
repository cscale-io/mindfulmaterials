from pydantic import BaseModel
from typing import Literal, Any

from ._substances import Substances
from ._vocs import VOCs

# Bucket models
class HumanHealth(BaseModel):
    substances: Substances
    vocs: VOCs