from collections import defaultdict

def djikstra(neighbors_dict, weights_dict = defaultdict(lambda: 1), start_point = None, end_point = None, keep_paths = True, dist_est = lambda x: 0):
    visited = set()
    curr_point = start_point

    weights = {curr_point: 0}
    explore = {}
    if keep_paths:
        paths = {curr_point: [curr_point]}

    while True:
        if end_point is not None and curr_point == end_point:
            break
        visited.add(curr_point)
        if keep_paths:
            curr_path = paths[curr_point]
        if curr_point in neighbors_dict:
            for n in neighbors_dict[curr_point]:
                curr_weight = weights[curr_point] + weights_dict[(curr_point, n)]
                if n not in weights or curr_weight < weights[n]:
                    weights[n] = curr_weight
                    if keep_paths:
                        paths[n] = curr_path + [n]
                if n not in visited:
                    explore[n] = curr_weight + dist_est(n)

        if len(explore) == 0:
            break

        curr_point = min(explore.items(), key=lambda x: x[1])[0]
        del explore[curr_point]

    if keep_paths:
        return weights, paths

    return weights

class Dictlike():
    def __init__(self, get_fn, contains_fn = lambda x: True):
        self.get_fn = get_fn
        self.contains_fn = contains_fn

    def __getitem__(self, key):
        return self.get_fn(key)

    def __contains__(self, key):
        return self.contains_fn(key)
