from typing import List

class NumberStore:
    def __init__(self) -> None:
        self._data: List[int] = []

    def insert(self, value: int) -> None:
        self._data.append(value)

    def search(self, target: int) -> int:
        for i, v in enumerate(self._data, start=1):
            if v == target:
                return i
        return -1
