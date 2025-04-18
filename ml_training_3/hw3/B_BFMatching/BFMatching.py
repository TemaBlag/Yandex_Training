import numpy as  np

class DummyMatch:
    def __init__(self, queryIdx, trainIdx, distance):
        self.queryIdx = queryIdx  
        self.trainIdx = trainIdx  
        self.distance = distance

def match_key_points_numpy(des1: np.ndarray, des2: np.ndarray) -> list:
    matches = []
    des1_best_matches = {}
    des2_best_matches = {}

    for ind_i, i in enumerate(des1):
        best_distance = float('inf')
        best_j = -1
        for ind_j, j in enumerate(des2):
            distance = np.linalg.norm(i - j)
            if distance < best_distance:
                best_distance = distance
                best_j = ind_j
        des1_best_matches[ind_i] = (best_j, best_distance)

    for ind_j, j in enumerate(des2):
        best_distance = float('inf')
        best_i = -1
        for ind_i, i in enumerate(des1):
            distance = np.linalg.norm(j - i)
            if distance < best_distance:
                best_distance = distance
                best_i = ind_i
        des2_best_matches[ind_j] = (best_i, best_distance)

    for i, (j, dist) in des1_best_matches.items():
        best_i_for_j, _ = des2_best_matches[j]
        if best_i_for_j == i:
            matches.append(DummyMatch(i, j, dist))

    matches.sort(key=lambda m: m.distance)
    return matches