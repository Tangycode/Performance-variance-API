from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import PerformanceVarianceRequest
from helpers.validation import validate_variance_inputs
from services.variance_service import (
    compute_mean,
    compute_variance,
    compute_overall_variance,
    stability_index,
    interpret_stability
)

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- HEALTH ----------------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Khel AI Performance Variance Service Running"}

# ---------------- API ----------------
@app.post("/api/v1/performance-variance")
def performance_variance(payload: PerformanceVarianceRequest):

    try:
        batting = payload.batting
        bowling = payload.bowling
        fielding = payload.fielding

        zero_flag = validate_variance_inputs(batting, bowling, fielding)

        # means
        batting_mean = compute_mean(batting)
        bowling_mean = compute_mean(bowling)
        fielding_mean = compute_mean(fielding)

        # variances
        batting_var = compute_variance(batting)
        bowling_var = compute_variance(bowling)
        fielding_var = compute_variance(fielding)

        overall_var = compute_overall_variance(batting, bowling, fielding)

        stability, note = stability_index(overall_var)

        # handle zero variance safely
        if zero_flag == "ZERO_VARIANCE":
            stability = 100
            note = "perfectly stable in supplied sample"

        interpretation = interpret_stability(stability)

        return {
            "player_id": payload.player_id,
            "player_name": payload.player_name,
            "match_window": payload.match_window,
            "recent_matches": payload.recent_matches,

            "mean_values": {
                "batting_mean": batting_mean,
                "bowling_mean": bowling_mean,
                "fielding_mean": fielding_mean
            },

            "variance_values": {
                "batting_variance": batting_var,
                "bowling_variance": bowling_var,
                "fielding_variance": fielding_var,
                "overall_variance": overall_var
            },

            "stability_index": stability,
            "interpretation": interpretation,
            "note": note
        }

    except ValueError as e:

        error_map = {
            "EMPTY_DATA": "Input arrays cannot be empty",
            "NON_NUMERIC_VALUES": "All values must be numeric",
            "INVALID_INPUT_TYPE": "Invalid input type detected"
        }

        err = str(e)

        raise HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "error_code": err,
                "message": error_map.get(err, "Validation error")
            }
        )
