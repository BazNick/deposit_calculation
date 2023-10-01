from fastapi import HTTPException
from fastapi import APIRouter
from .calculation import calculations

from src.schemes.schemes import ErrorMessages, DepositIn, DepositOut

router = APIRouter()


@router.post("/calculate-deposit/", response_model=DepositOut, responses={
    400: {"model": ErrorMessages}
})
def calculate_deposit(data: DepositIn):
    try:
        if not (1 <= data.periods <= 60):
            raise ValueError(ErrorMessages.PERIOD_ERROR.value)
        if not (10000 <= data.amount <= 3000000):
            raise ValueError(ErrorMessages.AMOUNT_ERROR.value)
        if not (1 <= data.rate <= 8):
            raise ValueError(ErrorMessages.RATE_ERROR.value)

        return calculations(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
