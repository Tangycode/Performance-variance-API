def validate_lengths(*lists):
    if len(set(len(lst) for lst in lists)) != 1:
        raise ValueError("All lists must have equal length")
