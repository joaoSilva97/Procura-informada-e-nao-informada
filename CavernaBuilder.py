def build():
    size = 30
    caverna = {}
    for x in range(1, size + 1):
        for y in range(1, size + 1):
            gridtemp = []

            if x > 1:
                gridtemp.append((x - 1, y))
            if x < size:
                gridtemp.append((x + 1, y))
            if y > 1:
                gridtemp.append((x, y - 1))
            if y < size:
                gridtemp.append((x, y + 1))

            caverna[(x, y)] = gridtemp

    return caverna

