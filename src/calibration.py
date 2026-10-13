def normalize_scores(scores, target_mean=3.0):
    """Калибровка: менеджеры ставят по-разному. Приводим к средней."""
    if not scores:
        return scores
    current_mean = sum(scores.values()) / len(scores)
    factor = target_mean / current_mean if current_mean else 1
    return {k: round(v * factor, 2) for k, v in scores.items()}
