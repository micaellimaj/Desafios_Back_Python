from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

# Schema base para dados comuns
class TransactionBase(BaseModel):
    amount: float = Field(..., gt=0, description="O valor deve ser maior que zero")
    description: Optional[str] = None

# Entrada para criar transação (o que o usuário envia)
class TransactionCreate(TransactionBase):
    type: str 

    @validator('type')
    def validate_type(cls, v):
        if v not in ["deposit", "withdrawal"]:
            raise ValueError("O tipo deve ser 'deposit' ou 'withdrawal'")
        return v

# Saída da transação (o que a API retorna no extrato)
class TransactionResponse(TransactionBase):
    id: int
    account_id: int
    type: str
    timestamp: datetime

    class Config:
        orm_mode = True