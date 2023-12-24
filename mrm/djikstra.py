from collections import defaultdict

def djikstra(neighbors_dict, weights_dict = defaultdict(lambda: 1), start_point = None, end_point = None, keep_paths = True, dist_est = lambda x: 0, danger_ignore_visited = False):
    visited = set()
    curr_point = start_point

    weights = {curr_point: 0}
    explore = defaultdict(set)
    if keep_paths:
        paths = {curr_point: [curr_point]}

    if isinstance(end_point, list):
        found_ends = {e: False for e in end_point}
    else:
        found_ends = {end_point: False}

    while True:
        if end_point is not None:
            if curr_point in found_ends:
                found_ends[curr_point] = True
            if curr_point == end_point:
                break
            if all(found_ends.values()):
                break
        if not danger_ignore_visited:
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
                    explore[curr_weight + dist_est(n)].add(n)

        buckets = sorted(explore.keys())
        while curr_point in visited or danger_ignore_visited:
            found_point = False
            for b in buckets:
                if len(explore[b]) != 0:
                    curr_point = explore[b].pop()
                    found_point = True
                    break
                del explore[b]
            if not found_point or danger_ignore_visited:
                break
        if not found_point:
            break

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
