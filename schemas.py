from pydantic import BaseModel, Field
from typing import List

class VarianceInput(BaseModel):
    batting_scores: List[float] = Field(..., min_items=2)
    bowling_scores: List[float] = Field(..., min_items=2)
    fielding_scores: List[float] = Field(..., min_items=2)

class VarianceResponse(BaseModel):
    success: bool
    batting_variance: float
    bowling_variance: float
    fielding_variance: float
    overall_variance: float
    stability_index: float
    interpretation: str
