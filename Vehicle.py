from Trail import Trail
from typing import List, Tuple
from Boost import Boost


class Vehicle:

    """
    Vehicle class for each vehicle object that will be added to game

    === Attributes ===
    x: x coordinate of the vehicle
    y: y coordinate of the vehicle

    === Representation Invariants ===
    x, y >= 0
    """
    x: int
    y: int
    width: int
    height: int
    color: Tuple[int, int, int]
    controls: List
    trail: Trail
    change: Tuple
    name: str
    is_boost: bool
    boost: Boost

    def __init__(self, x, y, width, height, color, controls, name):
        """
        Constructor for vehicle
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.trail = Trail(x, y, 1, color)
        self.controls = controls
        self.name = name
        self.is_boost = False
        self.boost = Boost(3, 3)
        self.change = (0, 0)


    def get_x(self) -> int:
        """
        returns x-value for vehicle
        """
        return self.x

    def get_y(self) -> int:
        """
        returns y-value for vehicle
        """
        return self.y

    def change_pos(self) -> None:
        """
        changes position for vehicle
        """
        self.x += self.change[0]
        self.y += self.change[1]
        self.trail.add_locations([(self.x, self.y + self.width/2)])

    def set_pos(self, position: Tuple[int, int]) -> None:
        """
        changes position for vehicle
        """
        self.x = position[0]
        self.y = position[1]
        self.trail.add_locations([(self.x, self.y + self.width/2)])

    def get_width(self) -> int:
        """
        returns width of vehicle
        """
        return self.width

    def get_height(self) -> int:
        """
        returns height of vehicle
        """
        return self.height

    def get_color(self) -> tuple:
        """
        returns color of vehicle in (r, g, b)
        """
        return self.color

    def get_trail(self) -> Trail:
        return self.trail

    def add_trail(self, locations: List[tuple]) -> None:
        self.trail.add_locations(locations)

    def get_controls(self) -> List:
        return self.controls

    def set_change(self, change: Tuple) -> None:
        self.change = change

    def get_name(self) -> str:
        return self.name

    def set_is_boost(self, boost: bool):
        self.is_boost = boost

    def get_is_boost(self) -> bool:
        return self.is_boost

    def get_boost(self) -> Boost:
        return self.boost
