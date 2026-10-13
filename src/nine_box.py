def grid_position(performance, potential):
    """Performance/Potential 1-5 → 3x3 grid."""
    def bucket(x):
        if x >= 4: return 2
        if x >= 3: return 1
        return 0
    return bucket(performance), bucket(potential)

def nine_box_label(perf_b, pot_b):
    labels = [
        ["Underperformer", "Inconsistent", "High Potential"],
        ["Effective", "Core Player", "Star"],
        ["Trusted Pro", "High Performer", "Top Talent"],
    ]
    return labels[pot_b][perf_b]

def plot_data(employees):
    return [{"name": e["name"],
             "performance": e["performance"],
             "potential": e["potential"],
             "label": nine_box_label(*grid_position(e["performance"], e["potential"]))}
            for e in employees]
