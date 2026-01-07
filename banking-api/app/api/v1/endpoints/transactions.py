from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.api.deps import get_current_user
from app.models.account import Account
from app.crud import crud_transaction
from typing import List
from sqlalchemy.future import select

router = APIRouter()

@router.post("/", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
async def make_transaction(
    transaction_in: TransactionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    """
    Realiza um depósito ou saque na conta do usuário autenticado.
    """
    return await crud_transaction.create_banking_transaction(
        db=db, 
        transaction_in=transaction_in, 
        account=current_user
    )


@router.get("/statement", response_model=List[TransactionResponse])
async def get_statement(
    db: AsyncSession = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    """
    Exibe todas as transações (depósitos e saques) da conta do usuário autenticado.
    """
    query = select(Transaction).filter(Transaction.account_id == current_user.id).order_by(Transaction.timestamp.desc())
    result = await db.execute(query)
    return result.scalars().all()