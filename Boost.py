
class Boost:

    max_boost: int
    curr_boost: int
    charge: int
    max_charge: int
    boost_length: int

    def __init__(self, max_boost: int, curr: int) -> None:
        self.max_boost = max_boost
        self.curr_boost = curr
        self.charge = 0
        self.max_charge = 1000
        self.boost_length = 150

    def get_max(self) -> int:
        return self.max_boost

    def get_curr(self) -> int:
        return self.curr_boost

    def change_boost(self, num: int) -> None:
        if num < 0:
            self.curr_boost += num
        elif num > 0 and self.curr_boost < self.max_boost:
            self.curr_boost += num

    def add_charge(self, num: int) -> None:
        if self.curr_boost < self.max_boost:
            self.charge += num
            if self.charge >= self.max_charge:
                self.charge = 0
                self.curr_boost += 1
        else:
            self.charge = 0

    def get_charge(self) -> int:
        return self.charge

    def get_max_charge(self) -> int:
        return self.max_charge

    def get_boost_length(self) -> int:
        return self.boost_length
