from Vehicle import Vehicle
from typing import Optional, Tuple


class PowerUp:

    width: int
    height: int
    x: int
    y: int
    power_up_num: int

    def __init__(self, width: int, height: int, x: int, y: int,
                 num: int) -> None:
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.power_up_num = num
        self.color = (0, 0, 0)

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_color(self) -> Tuple[int, int, int]:
        return self.color

    def activate(self, num: int, player: Optional[Vehicle]) -> Optional:
        switcher = {
            1: self.add_boost(player, 1)
        }
        switcher.get(num)

    def add_boost(self, player: Vehicle, num: int) -> None:
        boost = player.get_boost()
        boost.change_boost(num)

