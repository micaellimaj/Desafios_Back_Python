from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.account import Account
from app.schemas.account import AccountCreate
from app.core.security import get_password_hash

async def get_account_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(Account).filter(Account.email == email))
    return result.scalars().first()

async def create_account(db: AsyncSession, account_in: AccountCreate):
    hashed_pw = get_password_hash(account_in.password)
    db_account = Account(
        owner_name=account_in.owner_name,
        email=account_in.email,
        hashed_password=hashed_pw,
        balance=0.0
    )
    db.add(db_account)
    await db.commit()
    await db.refresh(db_account)
    return db_account