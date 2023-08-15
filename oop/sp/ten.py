from dataclasses import dataclass, field
from functools import total_ordering
from typing import List


@dataclass(frozen=True)
class Stock:
    ticker: str = field(compare=False)
    price: float
    dividend: float = field(default=0, compare=False)
    dividend_frequency: int = field(default=4, compare=False)

    @property
    def annual_dividend(self):
        return self.dividend * self.dividend_frequency


@total_ordering
@dataclass
class Position:
    stock: Stock
    shares: float

    def __eq__(self, other):
        return self.shares * self.stock.price == other.shares * other.stock.price

    def __gt__(self, other):
        return self.shares * self.stock.price > other.shares * other.stock.price


@dataclass
class Portfolio:
    holdings: List[Position]

    @property
    def value(self):
        return sum(map(lambda position: position.shares * position.stock.price, self.holdings))

    @property
    def portfolio_yield(self):
        return sum(map(lambda position: position.stock.annual_dividend * position.shares, self.holdings)) / self.value


MSFT = Stock('MSFT', 320, 0.62, 4)
LMT = Stock('LMT', 320, 3.2, 4)
GOOGL = Stock('GOOGL', 2800, 0, 0)
print(MSFT)
print(LMT)
print(GOOGL)
print(MSFT.annual_dividend)
print(LMT.annual_dividend)
print(GOOGL.annual_dividend)
p1 = Position(MSFT, 100)
p2 = Position(LMT, 100)
p3 = Position(GOOGL, 10)
print(p1==p2)
print(p1<=p3)
portfolio = Portfolio(holdings=[p1, p2, p3])
print(portfolio.portfolio_yield)
print(portfolio.value)

