class Road:
    def __init__(self, _length, _width, _thickness):
        self._length = _length
        self._width = _width
        self._thickness = _thickness

    def mass(self):
        return self._length * self._width * 25 * self._thickness / 1000


m = Road(float(input("длина дороги в м: ")), float(input("ширина дороги в м: ")),
         float(input("толщина слоя дороги в см: ")))
print(f' масса всего дорожного полотна равна {m.mass()} тонн')
