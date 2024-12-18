class Fibonacci:
    def __init__(self, n):
        if not isinstance(n, int):
            raise ValueError("Fibonacci sequence length must be an integer.")
        self.n = n
