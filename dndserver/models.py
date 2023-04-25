import arrow
from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Boolean, Enum, Integer, String, Text
from sqlalchemy_utils import ArrowType

from dndserver.database import db
from dndserver.enums import CharacterClass, Gender


base = declarative_base()


class Account(base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(20), unique=True, nullable=False)
    password = Column(Text)
    secret_token = Column(String(21))
    created_at = Column(ArrowType, default=arrow.utcnow())
    ban_type = Column(Integer)

    def save(self):
        db.add(self)
        db.commit()


class Character(base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    user_id = Column(Integer)
    nickname = Column(String(20), unique=True)
    gender = Column(Enum(Gender))
    character_class = Column(Enum(CharacterClass))
    created_at = Column(ArrowType, default=arrow.utcnow())
    level = Column(Integer, default=1)
    karma_rating = Column(Integer, default=0)

    def save(self):
        db.add(self)
        db.commit()

    def delete(self):
        db.delete(self)
        db.commit()


class Item(base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    account_id = Column(Integer, ForeignKey("accounts.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))
    item_id = Column(Integer, nullable=False)
    item_quantity = Column(Integer)
    inventory_id = Column(Integer)
    slot_id = Column(Integer)
    item_perk_one = Column(String, default=None)
    item_perk_two = Column(String, default=None)
    item_perk_three = Column(String, default=None)
    item_perk_four = Column(String, default=None)
    item_perk_five = Column(String, default=None)
    #item_ammo_count = Column(Integer)     not sure we need this server side
    #item_contents_count = Column(Integer) not sure we need this server side 

    def save(self):
        db.add(self)
        db.commit()
    
    def delete(self):
        db.delete(self)
        db.commit()


class Hwid(base):
    __tablename__ = "hwids"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    user_id = Column(Integer)
    hwid = Column(String(64), unique=True)
    is_banned = Column(Boolean)
    seen_at = Column(ArrowType, default=arrow.utcnow())


# class Login(base):
#     __tablename__ = "logins"
#     id = Column(Integer, primary_key=True, autoincrement="auto")

# characters: store all logins in a database and grab the latest from that
# Attempts to initialize the database for the first time.
