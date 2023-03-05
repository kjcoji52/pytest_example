from typing import Self

class Data:
    def __init__(self, value: float) -> None:
        self.value = value
    
    def add(self, other: Self):
        val = self.value + other.value
        return self.__class__(val)
    