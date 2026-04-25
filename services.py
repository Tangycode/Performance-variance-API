import statistics


def compute_mean(values):
    return sum(values) / len(values)


def compute_variance(values):
    mean = compute_mean(values)
    return sum((x - mean) ** 2 for x in values) / len(values)


def compute_overall_variance(b, bo, f):
    vb = compute_variance(b)
    vbo = compute_variance(bo)
    vf = compute_variance(f)

    return (vb + vbo + vf) / 3


def stability_index(overall_variance):
    if overall_variance == 0:
        return 100, "perfectly stable in supplied sample"

    return 1 / overall_variance, None


def interpret_stability(index):
    if index >= 10:
        return "Highly Stable"
    elif index >= 5:
        return "Stable"
    elif index >= 1:
        return "Volatile"
    else:
        return "Highly Volatile"
