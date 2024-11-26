import random

from collections import namedtuple
from typing_extensions import NamedTuple

Vec2i = NamedTuple("Vec2i", [("x", int), ("y",int)])

class Maze:
    def __init__(self, width: int, height: int) -> None:
        self._cells: bytes = bytes(width*height)
        self.width: int = width
        self.height: int = height
    
    def get_tile(self, x: int, y: int) -> int:
        return self._cells[self.width * y + x]

    def set_tile(self, x: int, y: int, value: int) -> int:
        self._cells[self.width * y + x] = value

    def tile_neighbors(self, x: int, y: int) -> list[Vec2i]:
        ret : list[Vec2i]
        
        if 0 < x:
            ret.append(Vec2i(x - 1, y))

        if x < self.width - 1:
            ret.append(Vec2i(x + 1, y))

        if 0 < y:
            ret.append(Vec2i(x, y - 1))

        if y < self.height - 1:
            ret.append(Vec2i(x, y + 1))

        return ret

    def generate(self):
        checks: set[Vec2i] = {}
        pos: Vec2i = (0, 0)


if __name__ == "__main__":
    pass