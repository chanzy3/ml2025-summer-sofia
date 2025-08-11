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

def read_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Please enter an integer.")

def read_positive_int(prompt: str) -> int:
    while True:
        n = read_int(prompt)
        if n > 0:
            return n
        print("Please enter a positive integer (> 0).")

def main() -> None:
    store = NumberStore()
    n = read_positive_int("Enter N (positive integer): ")
    for i in range(1, n + 1):
        val = read_int(f"Enter number #{i}: ")
        store.insert(val)
    x = read_int("Enter X (integer to search for): ")
    idx = store.search(x)
    print(idx)

if __name__ == "__main__":
    main()
