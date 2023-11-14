from sqlalchemy import  Column, Integer, String, Float, Boolean


from database_conf import Base, SessionLocal, engine

# Define the base class
session = SessionLocal()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String)
    username = Column(String)
    balance = Column(Float)
    role = Column(Integer)
    active = Column(Boolean)

    def __repr__(self):
        return f"<User(id={self.id}, telegram_id='{self.telegram_id}', username='{self.username}', balance={self.balance}, role={self.role}, active={self.active})>"


# Create the User table
Base.metadata.create_all(engine)


# CRUD Operations for User
def add_user(telegram_id, username, balance, role, active):
    new_user = User(telegram_id=telegram_id, username=username, balance=balance, role=role, active=active)
    session.add(new_user)
    session.commit()
    return new_user


def get_all_users():
    return session.query(User).all()


def get_user_by_id(user_id):
    return session.query(User).filter(User.id == user_id).first()


def update_user(user_id, new_telegram_id=None, new_username=None, new_balance=None, new_role=None, new_active=None):
    user_to_update = session.query(User).filter(User.id == user_id).first()
    if user_to_update:
        if new_telegram_id is not None:
            user_to_update.telegram_id = new_telegram_id
        if new_username is not None:
            user_to_update.username = new_username
        if new_balance is not None:
            user_to_update.balance = new_balance
        if new_role is not None:
            user_to_update.role = new_role
        if new_active is not None:
            user_to_update.active = new_active
        session.commit()
        return user_to_update
    return None


def delete_user(user_id):
    user_to_delete = session.query(User).filter(User.id == user_id).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        return True
    return False


# Example Usage
# Add a new user
new_user = add_user("123456789", "john_doe", 100.0, 1, True)

# Update the user
updated_user = update_user(new_user.id, new_balance=150.0, new_active=False)

# Delete the user
delete_status = delete_user(new_user.id)
