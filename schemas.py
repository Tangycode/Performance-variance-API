from pydantic import BaseModel, Field
from typing import List, Optional


class PerformanceVarianceRequest(BaseModel):
    match_id: str = Field(..., min_length=1)
    innings_id: str = Field(..., min_length=1)

    player_id: str
    player_name: str

    match_window: Optional[str] = "recent"
    recent_matches: Optional[int] = 5

    batting: List[float]
    bowling: List[float]
    fielding: List[float]

    ball_events: Optional[list] = []
