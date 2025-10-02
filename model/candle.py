from dataclasses import dataclass, asdict


@dataclass
class MinuteCandle:
    symbol: str
    price: float
    volume: int

    def to_dict(self):
        return asdict(self)
