def is_above_threshold(value, threshold):
    return value >= threshold


def is_within_range(value, min_val, max_val):
    return min_val <= value <= max_val


def has_required_keys(data, required_keys):
    return all(key in data for key in required_keys)