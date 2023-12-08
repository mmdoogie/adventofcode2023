def adj_ortho(pt, constrain_pos = None):
    adj = [(pt[0] - 1, pt[1]), (pt[0] + 1, pt[1]), (pt[0], pt[1] - 1), (pt[0], pt[1] + 1)]
    if constrain_pos is None:
        return adj
    return [a for a in adj if a in constrain_pos]

def adj_diag(pt, constrain_pos = None):
    adj = [(pt[0] - 1, pt[1] - 1), (pt[0],     pt[1] - 1), (pt[0] + 1, pt[1] - 1),
           (pt[0] - 1, pt[1]    ),                         (pt[0] + 1, pt[1]    ),
           (pt[0] - 1, pt[1] + 1), (pt[0],     pt[1] + 1), (pt[0] + 1, pt[1] + 1)]
    if constrain_pos is None:
        return adj
    return [a for a in adj if a in constrain_pos]

def m_dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

