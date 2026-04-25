# Khel AI Performance Variance Model

## Purpose
Measures player performance stability using batting, bowling, and fielding variance.

---

## Endpoint
POST /api/v1/performance-variance

---

## Input Schema
- match_id
- innings_id
- player_id
- player_name
- match_window
- recent_matches
- batting (List[float])
- bowling (List[float])
- fielding (List[float])

---

## Output Schema
- mean_values
- variance_values
- stability_index
- interpretation
- note

---

## Stability Scale

| Range | Label |
|------|------|
| ≥10 | Highly Stable |
| 5–10 | Stable |
| 1–5 | Volatile |
| <1 | Highly Volatile |

---

## Special Case
- If variance = 0:
  - stability_index = 100
  - note = "perfectly stable in supplied sample"

---

## Error Codes
- EMPTY_DATA
- NON_NUMERIC_VALUES
- INVALID_INPUT_TYPE

---

## Notes
- Fully stateless computation
- Uses mean + variance decomposition
- Designed for player performance consistency tracking
