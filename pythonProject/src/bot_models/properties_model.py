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


# Create an engine and session


# CRUD Operations
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


# Example Usage
# Add a new property
property_1 = add_property("way1", "value1")

# Get all properties
all_properties = get_all_properties()

# Update a property
updated_property = update_property(property_1.id, new_way="new_way2", new_value="value2")

# Delete a property
delete_status = delete_property(property_1.id)
