
from pydantic import BaseModel

class CashbackCreditOut(BaseModel):
    credit:int
class CashbackOut(BaseModel):
    statusCode:int
    body:CashbackCreditOut
