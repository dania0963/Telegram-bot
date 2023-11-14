from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from src.bot_models.users_model import User
from database_conf import Base, SessionLocal, engine


# Define the base class
session = SessionLocal()


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationship to the User model
    user = relationship("User", back_populates="players")

    def __repr__(self):
        return f"<Player(id={self.id}, name='{self.name}', user_id={self.user_id})>"


# Add a relationship to the User model
User.players = relationship("Player", order_by=Player.id, back_populates="user")

# Create the Player table
Base.metadata.create_all(engine)


# CRUD Operations for Player
def add_player(name, password, user_id):
    new_player = Player(name=name, password=password, user_id=user_id)
    session.add(new_player)
    session.commit()
    return new_player


def get_all_players():
    return session.query(Player).all()


def get_player_by_id(player_id):
    return session.query(Player).filter(Player.id == player_id).first()


def update_player(player_id, new_name=None, new_password=None, new_user_id=None):
    player_to_update = session.query(Player).filter(Player.id == player_id).first()
    if player_to_update:
        if new_name is not None:
            player_to_update.name = new_name
        if new_password is not None:
            player_to_update.password = new_password
        if new_user_id is not None:
            player_to_update.user_id = new_user_id
        session.commit()
        return player_to_update
    return None


def delete_player(player_id):
    player_to_delete = session.query(Player).filter(Player.id == player_id).first()
    if player_to_delete:
        session.delete(player_to_delete)
        session.commit()
        return True
    return False


# Example Usage
# Add a new player (assuming a user with user_id already exists)
new_player = add_player("player1", "pass123", 1)

# Update the player
updated_player = update_player(new_player.id, new_name="player2")

# Delete the player
delete_status = delete_player(new_player.id)
