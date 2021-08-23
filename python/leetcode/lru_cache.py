from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache.keys():
            self.cache.popitem(last=False)

        self.cache[key] = value
        self.cache.move_to_end(key)


def main():
    pass


if __name__ == "__main__":
    main()
