def simple_map(transformation, values):
    sp = []
    for i in values:
        sp.append(transformation(i))
    return sp