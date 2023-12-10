from itertools import product

ZERO_2D = (0, 0)
ZERO_3D = (0, 0, 0)

def adj_ortho(pt, constrain_pos = None):
    dims = len(pt)
    adj = [(*pt[:d], pt[d] + o, *pt[d + 1:]) for d in range(dims) for o in [-1, 1]]
    if constrain_pos is None:
        return adj
    return [a for a in adj if a in constrain_pos]

def adj_diag(pt, constrain_pos = None):
    dims = len(pt)
    adj = [tuple(pt[i] + o[i] for i in range(dims)) for o in product([-1, 0, 1], repeat = dims) if any(o)]
    if constrain_pos is None:
        return adj
    return [a for a in adj if a in constrain_pos]

def m_dist(pt1, pt2):
    if len(pt1) != len(pt2):
        raise ValueError('Point lengths must match to compute distance')
    return sum(abs(a - b) for a, b in zip(pt1, pt2))

def point_add(pt1, pt2):
    return tuple(a + b for a, b in zip(pt1, pt2))

def point_sub(pt1, pt2):
    return tuple(a - b for a, b in zip(pt1, pt2))

def point_neg(pt):
    return tuple(-p for p in pt)
