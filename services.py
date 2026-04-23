def calculate_variance(data):
    b = data.batting_scores
    bo = data.bowling_scores
    f = data.fielding_scores

    if not (len(b) == len(bo) == len(f)):
        raise ValueError("All input lists must have the same length")

    def variance(arr):
        n = len(arr)
        mean = sum(arr) / n
        return sum((x - mean) ** 2 for x in arr) / n

    var_batting = variance(b)
    var_bowling = variance(bo)
    var_fielding = variance(f)

    overall_variance = (var_batting + var_bowling + var_fielding) / 3

    if overall_variance == 0:
        stability_index = float('inf')
    else:
        stability_index = 1 / overall_variance

    if overall_variance < 0.01:
        interpretation = "Highly Stable"
    elif overall_variance < 0.05:
        interpretation = "Moderately Stable"
    else:
        interpretation = "Unstable"

    return {
        "success": True,
        "batting_variance": round(var_batting, 4),
        "bowling_variance": round(var_bowling, 4),
        "fielding_variance": round(var_fielding, 4),
        "overall_variance": round(overall_variance, 4),
        "stability_index": round(stability_index, 2) if stability_index != float('inf') else stability_index,
        "interpretation": interpretation
    }
