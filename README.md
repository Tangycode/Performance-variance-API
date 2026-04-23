# Performance Variance Model API

## Endpoint
POST /api/v1/performance-variance

## Description
Measures consistency of an all-rounder across batting, bowling, and fielding using variance.

## Input
{
  "batting_scores": [...],
  "bowling_scores": [...],
  "fielding_scores": [...]
}

## Output
{
  "success": true,
  "batting_variance": float,
  "bowling_variance": float,
  "fielding_variance": float,
  "overall_variance": float,
  "stability_index": float,
  "interpretation": string
}

## Run
pip install -r requirements.txt
uvicorn main:app --reload
