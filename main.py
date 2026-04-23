from fastapi import FastAPI, HTTPException
from schemas import VarianceInput, VarianceResponse
from services import calculate_variance
import logging

app = FastAPI(title="Performance Variance Model API", version="1.0")

logging.basicConfig(level=logging.INFO)

@app.post("/api/v1/performance-variance", response_model=VarianceResponse)
def performance_variance(data: VarianceInput):
    try:
        logging.info("Variance analysis request received")
        return calculate_variance(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
