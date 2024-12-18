class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Fibonacci sequence length must be an integer.")
        self.n = max(0, n)  # Handle negative values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0 and self.n == 0:
            self.index += 1
            return 0
        raise StopIteration
