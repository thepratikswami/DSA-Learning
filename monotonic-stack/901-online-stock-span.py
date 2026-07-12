class StockSpanner:
    def __init__(self) -> None:
        self.stack = []  # holds (price, span) with strictly decreasing prices

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# DEBUG RUNNER START
if __name__ == "__main__":
    spanner = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    print([spanner.next(p) for p in prices])  # [1, 1, 1, 2, 1, 4, 6]
# DEBUG RUNNER END
