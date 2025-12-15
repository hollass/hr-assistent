import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def cosine_sim(vec1: list[float], vec2: list[float]) -> float:
    v1 = np.array(vec1).reshape(1, -1)
    v2 = np.array(vec2).reshape(1, -1)
    return float(cosine_similarity(v1, v2)[0][0])