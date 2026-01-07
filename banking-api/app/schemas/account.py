from pydantic import BaseModel, EmailStr, Field

class AccountCreate(BaseModel):
    owner_name: str
    email: EmailStr
    password: str = Field(..., min_length=6)

class AccountResponse(BaseModel):
    id: int
    owner_name: str
    email: EmailStr
    balance: float

    class Config:
        orm_mode = True