from typing import Callable


class Vec3:
    def __init__(self, x: int = 0, y: int = 0, z: int = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, rhs: "Vec3") -> "Vec3":
        c: Vec3 = self.clone()
        c += rhs
        return c

    def __iadd__(self, rhs: "Vec3") -> "Vec3":
        self.x += rhs.x
        self.y += rhs.y
        self.z += rhs.z
        return self

    def length(self) -> int | float:
        return self.lengthSqr() ** 0.5

    def lengthSqr(self) -> int:
        return self.x * self.x + self.y * self.y + self.z * self.z

    def __mul__(self, k: int | float) -> "Vec3":
        c = self.clone()
        c *= k
        return c

    def __imul__(self, k: int | float) -> "Vec3":
        self.x *= k
        self.y *= k
        self.z *= k
        return self

    def clone(self) -> "Vec3":
        return Vec3(self.x, self.y, self.z)

    def __neg__(self) -> "Vec3":
        return Vec3(-self.x, -self.y, -self.z)

    def __sub__(self, rhs: "Vec3") -> "Vec3":
        return self.__add__(-rhs)

    def __isub__(self, rhs: "Vec3") -> "Vec3":
        return self.__iadd__(-rhs)

    def __repr__(self):
        return "Vec3(%s,%s,%s)" % (self.x, self.y, self.z)

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def _map(self, func: Callable[[int], int]) -> None:
        self.x = func(self.x)
        self.y = func(self.y)
        self.z = func(self.z)

    def __cmp__(self, rhs: "Vec3") -> int:
        dx: int = self.x - rhs.x
        if dx != 0:
            return dx
        dy: int = self.y - rhs.y
        if dy != 0:
            return dy
        dz: int = self.z - rhs.z
        if dz != 0:
            return dz
        return 0

    def __eq__(self, rhs: "Vec3") -> bool:
        if self.x == rhs.x and self.y == rhs.y and self.z == rhs.z:
            return True

        return False

    def iround(self) -> None:
        self._map(lambda v: int(v + 0.5))

    def ifloor(self) -> None:
        self._map(int)

    def rotateLeft(self) -> None:
        self.x, self.z = self.z, -self.x

    def rotateRight(self) -> None:
        self.x, self.z = -self.z, self.x


def testVec3() -> None:
    # Note: It's not testing everything

    # 1.1 Test initialization
    it: Vec3 = Vec3(1, -2, 3)
    assert it.x == 1
    assert it.y == -2
    assert it.z == 3

    assert it.x != -1
    assert it.y != +2
    assert it.z != -3

    # 2.1 Test cloning and equality
    clone: Vec3 = it.clone()
    assert it == clone
    it.x += 1
    assert it != clone

    # 3.1 Arithmetic
    a: Vec3 = Vec3(10, -3, 4)
    b: Vec3 = Vec3(-7, 1, 2)
    c: Vec3 = a + b
    assert c - a == b
    assert c - b == a
    assert a + a == a * 2

    assert a - a == Vec3(0, 0, 0)
    assert a + (-a) == Vec3(0, 0, 0)

    # Test repr
    e: Vec3 = eval(repr(it))
    assert e == it


if __name__ == "__main__":
    testVec3()
