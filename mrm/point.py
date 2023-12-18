from itertools import pairwise, product

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

def dist(pt1, pt2):
    if len(pt1) != len(pt2):
        raise ValueError('Point lengths must match to compute distance')
    return sum((a - b) ** 2 for a, b in zip(pt1, pt2)) ** 0.5

def point_add(pt1, pt2):
    return tuple(a + b for a, b in zip(pt1, pt2))

def point_sub(pt1, pt2):
    return tuple(a - b for a, b in zip(pt1, pt2))

def point_neg(pt):
    return tuple(-p for p in pt)

def grid_as_dict(grid):
    res = {}
    for y, g in enumerate(grid):
        for x, c in enumerate(g):
            res[(x, y)] = c
    return res

def polygon_area(pts):
    x = [p[0] for p in pts]
    y = [p[1] for p in pts]
    if x[0] != x[-1] or y[0] != y[-1]:
        x += [x[0]]
        y += [y[0]]
    cross1 = sum(x1 * y2 for x1, y2 in zip(x, y[1:]))
    cross2 = sum(x2 * y1 for x2, y1 in zip(x[1:], y))
    if cross2 < cross1:
        return (cross1 - cross2) / 2
    return (cross2 - cross1) / 2

def polygon_border_dist(pts, dist_fn = m_dist):
    pts = list(pts)
    if pts[0] != pts[-1]:
        pts += [pts[0]]
    return sum(dist_fn(a, b) for a, b in pairwise(pts))

def polygon_interior_squares(pts, border_dist_fn = m_dist):
    area = polygon_area(pts)
    border = polygon_border_dist(pts, border_dist_fn)
    return area - border / 2 + 1

def polygon_grid_squares(pts, border_dist_fn = m_dist):
    return polygon_interior_squares(pts, border_dist_fn) + polygon_border_dist(pts, border_dist_fn)
