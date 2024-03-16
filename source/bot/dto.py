from dataclasses import dataclass


@dataclass
class ChangeCurrencyResponse:
    status: bool
    message: str
