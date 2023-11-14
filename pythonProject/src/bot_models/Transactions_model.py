from sqlalchemy import ForeignKey, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from database_conf import Base, SessionLocal, engine


# Define the base class
session = SessionLocal()


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String)
    way = Column(String)
    value = Column(Float)
    date = Column(DateTime, default=func.now())
    status = Column(String)
    specifics = Column(JSON)

    # Relationship to the User model
    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])

    def __repr__(self):
        return f"<Transaction(id={self.id}, sender_id={self.sender_id}, receiver_id={self.receiver_id}, type='{self.type}', value={self.value}, date={self.date}, status='{self.status}')>"


# Create the Transaction table
Base.metadata.create_all(engine)


# CRUD Operations for Transaction
def add_transaction(sender_id, receiver_id, type, way, value, status, specifics):
    new_transaction = Transaction(sender_id=sender_id, receiver_id=receiver_id, type=type, way=way, value=value,
                                  status=status, specifics=specifics)
    session.add(new_transaction)
    session.commit()
    return new_transaction


def get_all_transactions():
    return session.query(Transaction).all()


def get_transaction_by_id(transaction_id):
    return session.query(Transaction).filter(Transaction.id == transaction_id).first()


def update_transaction(transaction_id, new_type=None, new_way=None, new_value=None, new_status=None,
                       new_specifics=None):
    transaction_to_update = session.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction_to_update:
        if new_type is not None:
            transaction_to_update.type = new_type
        if new_way is not None:
            transaction_to_update.way = new_way
        if new_value is not None:
            transaction_to_update.value = new_value
        if new_status is not None:
            transaction_to_update.status = new_status
        if new_specifics is not None:
            transaction_to_update.specifics = new_specifics
        session.commit()
        return transaction_to_update
    return None


def delete_transaction(transaction_id):
    transaction_to_delete = session.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction_to_delete:
        session.delete(transaction_to_delete)
        session.commit()
        return True
    return False


# Example Usage
# Add a new transaction (assuming sender and receiver users exist)
new_transaction = add_transaction(1, 2, "transfer", "online", 100.0, "pending", {"details": "example"})

# Update the transaction
updated_transaction = update_transaction(new_transaction.id, new_status="completed")

# Delete the transaction
delete_status = delete_transaction(new_transaction.id)
