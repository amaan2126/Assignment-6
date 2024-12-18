class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Fibonacci sequence length must be an integer.")
        self.n = max(0, n)
        self.index = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.n:
            raise StopIteration
        if self.index == 0:
            self.index += 1
            return self.a
        elif self.index == 1:
            self.index += 1
            return self.b
        else:
            next_value = self.a + self.b
            self.a, self.b = self.b, next_value
            self.index += 1
            return next_value

