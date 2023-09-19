class Vector3f:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


class Celestial:
    def __init__(self, mass, position, name):
        self.mass = float(mass)
        self.position = Vector3f(position.x, position.y, position.z)
        self.name = name

    def prt_pos(self):
        print(self.position.x, self.position.y, self.position.z)


class ArrayExtended:
    def __init__(self):
        self.index = []

    def list_members(self):
        if len(self.index) == 0:
            print("No items in array")
        for i in self.index:
            print(i.name)


def main():
    entities = ArrayExtended()
    entities.index.append(Celestial(50, Vector3f(6, 4, 3), "Cro"))  # = [Celestial(50, start_position, "Cro")]
    entities.list_members()
    entities.index[0].prt_pos()


main()
