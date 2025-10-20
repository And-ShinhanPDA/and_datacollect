from dataclasses import dataclass, asdict


@dataclass
class DailySnapshot:
    symbol: str
    prevClose: float
    prevVolume: int
    openPrice: float
    high52w: float
    low52w: float

    def to_dict(self):
        return asdict(self)
