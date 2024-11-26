import random

type Vec2i = tuple[int, int]

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
        
        if (x > 0)

    def generate(self):
        checks: set[Vec2i] = {}
        pos: Vec2i = (0, 0)


if __name__ == "__main__":
    pass