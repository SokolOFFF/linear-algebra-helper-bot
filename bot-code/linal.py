# TODO: implement all needed classes

class Vector:
    def _init_(self, size, *coordinates):
        self.size = size
        self.coordinates = coordinates

    def __add__(self, other):
        if self.size == 3:
            cx = self.coordinates[1]*other.coordinates[2] - self.coordinates[2]*other.coordinates[1]
            cy = self.coordinates[2]*other.coordinates[0] - self.coordinates[0]*other.coordinates[2]
            cz = self.coordinates[0]*other.coordinates[1] - self.coordinates[1]*other.coordinates[0]
            new_coordinates = [cx, cy, cz]
            return Vector(3, new_coordinates)
        else:
            return -1

    def __mul__(self, other):
        if self.size == other.size:
            answer = 0
            for i in range(self.size):
                answer = answer + self.coordinates[i]*other.coordinates[i]
            return answer
        else:
            return -1


