from sqlalchemy.ext.asyncio import AsyncSession
from app.models.account import Account
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate
from fastapi import HTTPException, status

async def create_banking_transaction(
    db: AsyncSession, 
    transaction_in: TransactionCreate, 
    account: Account
):
    # Logica de Saque
    if transaction_in.type == "withdrawal":
        if account.balance < transaction_in.amount:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Saldo insuficiente para realizar o saque."
            )
        account.balance -= transaction_in.amount
    
    # Logica de Depósito
    elif transaction_in.type == "deposit":
        account.balance += transaction_in.amount

    # Cria o registro da transação
    db_transaction = Transaction(
        amount=transaction_in.amount,
        type=transaction_in.type,
        account_id=account.id
    )
    
    db.add(db_transaction)
    # O SQLAlchemy marca o objeto 'account' como modificado automaticamente
    await db.commit()
    await db.refresh(db_transaction)
    return db_transaction