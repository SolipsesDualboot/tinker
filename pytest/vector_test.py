class Vertex:
    def __init__(self, a, b, c):
        self.x = float(a)
        self.y = float(b)
        self.z = float(c)


class PhysObject:
    def __init__(self, pos, rot):
        self.position = Vertex(pos[0], pos[1], pos[2])
        self.rotation = Vertex(rot[0], pos[1], pos[2])


new0 = PhysObject((10, 20, 30), (40, 50, 60))
print(new0.position.x)
