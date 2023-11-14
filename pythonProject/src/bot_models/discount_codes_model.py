# Assuming the previous setup for Base, engine, and session
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean

from sqlalchemy import Boolean, Float

from database_conf import Base, SessionLocal, engine

# Define the base class
session = SessionLocal()


class DiscountCode(Base):
    __tablename__ = 'discount_code'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    value = Column(Float)
    active = Column(Boolean)
    telegram_id = Column(String)

    def __repr__(self):
        return f"<DiscountCode(id={self.id}, code='{self.code}', value={self.value}, active={self.active}, telegram_id='{self.telegram_id}')>"


# Create the DiscountCode table
Base.metadata.create_all(engine)


# CRUD Operations for DiscountCode
def add_discount_code(code, value, active, telegram_id):
    new_discount_code = DiscountCode(code=code, value=value, active=active, telegram_id=telegram_id)
    session.add(new_discount_code)
    session.commit()
    return new_discount_code


def get_all_discount_codes():
    return session.query(DiscountCode).all()


def get_discount_code_by_id(code_id):
    return session.query(DiscountCode).filter(DiscountCode.id == code_id).first()


def update_discount_code(code_id, new_code=None, new_value=None, new_active=None, new_telegram_id=None):
    code_to_update = session.query(DiscountCode).filter(DiscountCode.id == code_id).first()
    if code_to_update:
        if new_code is not None:
            code_to_update.code = new_code
        if new_value is not None:
            code_to_update.value = new_value
        if new_active is not None:
            code_to_update.active = new_active
        if new_telegram_id is not None:
            code_to_update.telegram_id = new_telegram_id
        session.commit()
        return code_to_update
    return None


def delete_discount_code(code_id):
    code_to_delete = session.query(DiscountCode).filter(DiscountCode.id == code_id).first()
    if code_to_delete:
        session.delete(code_to_delete)
        session.commit()
        return True
    return False


# Example Usage
# Add a new discount code
discount_code = add_discount_code("SAVE10", 10.0, True, "123456789")

# Update the discount code
updated_discount_code = update_discount_code(discount_code.id, new_value=15.0, new_active=False)

# Delete the discount code
delete_status = delete_discount_code(discount_code.id)
