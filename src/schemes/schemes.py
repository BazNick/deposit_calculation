from enum import Enum
from pydantic import BaseModel
from typing import Dict


class ErrorMessages(Enum):
    PERIOD_ERROR = 'Периоды должны иметь значения от 1 до 60'
    AMOUNT_ERROR = 'Сумма должна иметь значения от 10 000 до 3 000 000'
    RATE_ERROR = 'Процент по вкладу должен иметь значение от 1 до 8'


class DepositIn(BaseModel):
    date: str
    periods: int
    amount: float
    rate: float


class DepositOut(BaseModel):
    results: Dict[str, float]
