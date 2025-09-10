from pydantic import BaseModel, ConfigDict
from typing import Literal, Any

from ._substances import Substances
from ._vocs import VOCs

# Bucket models
class HumanHealth(BaseModel):
    model_config = ConfigDict(extra='forbid')

    substances: Substances
    vocs: VOCs