from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db.session import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    owner_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
    transactions = relationship("Transaction", back_populates="account")