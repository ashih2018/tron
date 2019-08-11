from typing import List, Tuple


class Trail:

    width: int
    color: tuple
    capacity: int
    locations: List[tuple]

    """
    Trail class for each vehicle object that will be added to game

    === Attributes ===
    width: width of the trail
    location: all locations which the trail is present
    """

    def __init__(self, x, y, width, color):
        self.width = width
        self.locations = [(x, y)]
        self.color = color
        self.capacity = 1000

    def add_locations(self, new_loc: List[tuple]) -> None:
        """
        Adds new location to the list of location this trail exists at
        """
        for location in new_loc:
            if location in self.locations:
                self.locations.remove(location)
                self.locations.append(location)
            else:
                self.locations.append(location)
        while len(self.locations) > self.capacity:
            self.locations.pop(0)

    def exists(self, x: int, y: int) -> bool:
        """
        Returns whether or not line exists on specified point
        """
        if (x, y) in self.locations:
            return True
        return False

    def remove(self) -> Tuple[int, int]:
        """
        Removes first location in locations
        """
        return self.locations.pop(0)

    def get_color(self) -> tuple:
        """
        returns color of vehicle in (r, g, b)
        """
        return self.color

    def get_locations(self) -> List[Tuple]:
        return self.locations

    def get_width(self) -> int:
        return self.width
