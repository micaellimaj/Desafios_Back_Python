from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.account import AccountCreate, AccountResponse
from app.crud import crud_account

router = APIRouter()

@router.post("/", response_model=AccountResponse)
async def register_account(account_in: AccountCreate, db: AsyncSession = Depends(get_db)):
    user = await crud_account.get_account_by_email(db, account_in.email)
    if user:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    return await crud_account.create_account(db, account_in)