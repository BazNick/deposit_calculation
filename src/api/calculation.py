from datetime import datetime
from src.schemes.schemes import DepositIn, DepositOut
from dateutil.relativedelta import relativedelta


def calculations(data: DepositIn) -> DepositOut:
    start_date = datetime.strptime(data.date, "%d.%m.%Y")

    results = {}

    current_amount = data.amount
    for i in range(data.periods):
        current_amount *= (1 + data.rate / 12 / 100)
        current_date = (start_date + relativedelta(months=i)).strftime("%d.%m.%Y")
        results[current_date] = round(current_amount, 2)

    return DepositOut(results=results)
