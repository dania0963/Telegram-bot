from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database_conf import Base, SessionLocal

# Define the base class
session = SessionLocal()


# Define the Property model
class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    way = Column(String)
    value = Column(String)

    def __repr__(self):
        return f"<Property(id={self.id}, way='{self.way}', value='{self.value}')>"


# Define the ExchangeRate model
class ExchangeRate(Base):
    __tablename__ = 'exchange_rate'

    id = Column(Integer, primary_key=True)
    from_currency = Column(String)
    to_currency = Column(String)
    value = Column(Integer)

    def __repr__(self):
        return f"<ExchangeRate(id={self.id}, from_currency='{self.from_currency}', to_currency='{self.to_currency}', value={self.value})>"


# CRUD Operations for Property
def add_property(way, value):
    new_property = Property(way=way, value=value)
    session.add(new_property)
    session.commit()
    return new_property


def get_all_properties():
    return session.query(Property).all()


def get_property_by_id(property_id):
    return session.query(Property).filter(Property.id == property_id).first()


def update_property(property_id, new_way=None, new_value=None):
    property_to_update = session.query(Property).filter(Property.id == property_id).first()
    if property_to_update:
        if new_way is not None:
            property_to_update.way = new_way
        if new_value is not None:
            property_to_update.value = new_value
        session.commit()
        return property_to_update
    return None


def delete_property(property_id):
    property_to_delete = session.query(Property).filter(Property.id == property_id).first()
    if property_to_delete:
        session.delete(property_to_delete)
        session.commit()
        return True
    return False


# CRUD Operations for ExchangeRate
def add_exchange_rate(from_currency, to_currency, value):
    new_exchange_rate = ExchangeRate(from_currency=from_currency, to_currency=to_currency, value=value)
    session.add(new_exchange_rate)
    session.commit()
    return new_exchange_rate


def get_all_exchange_rates():
    return session.query(ExchangeRate).all()


def get_exchange_rate_by_id(rate_id):
    return session.query(ExchangeRate).filter(ExchangeRate.id == rate_id).first()


def update_exchange_rate(rate_id, new_from_currency=None, new_to_currency=None, new_value=None):
    rate_to_update = session.query(ExchangeRate).filter(ExchangeRate.id == rate_id).first()
    if rate_to_update:
        if new_from_currency is not None:
            rate_to_update.from_currency = new_from_currency
        if new_to_currency is not None:
            rate_to_update.to_currency = new_to_currency
        if new_value is not None:
            rate_to_update.value = new_value
        session.commit()
        return rate_to_update
    return None


def delete_exchange_rate(rate_id):
    rate_to_delete = session.query(ExchangeRate).filter(ExchangeRate.id == rate_id).first()
    if rate_to_delete:
        session.delete(rate_to_delete)
        session.commit()
        return True
    return False


# Example Usage
# Add and manipulate properties
property_1 = add_property("way1", "value1")
updated_property = update_property(property_1.id, new_way="new_way2", new_value="value2")
delete_status = delete_property(property_1.id)

# Add and manipulate exchange rates
exchange_rate = add_exchange_rate("USD", "EUR", 100)
updated_rate = update_exchange_rate(exchange_rate.id, new_value=105)
delete_status_rate = delete_exchange_rate(exchange_rate.id)
