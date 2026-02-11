import math


def average_valid_measurements(values):
    total = 0.0
    count = 0

    for v in values:
        if v is None:
            continue
        try:
            val = float(v)
        except (TypeError, ValueError):
            continue
        if not math.isfinite(val):
            continue
        total += val
        count += 1

    if count == 0:
        return 0

    return total / count
