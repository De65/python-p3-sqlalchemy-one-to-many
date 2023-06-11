# import datetime
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///one_to_many.db')

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

# class Customer(Base):
#     __tablename__='customers'
#     id=Column(Integer(),primary_key=True)
#     orders=relationship('order',backref='customer')

# class Order(Base):
#     __tablename__= 'orders'
#     id=Column(Integer(),primary_key=True)
#     customer_id=Column(Integer(),ForeignKey('customers.id'))

# class Order_metadata(Base):
#     __tablename__='orders_metadata'
#     id=Column(Integer(), primary_key=True)
#     order_id=Column(Integer(),ForeignKey('order.id'))

#     order=relationship('order',backref=backref('order_metadata',uselist=False))


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String(50))
    genre = Column(String(50))
    platform = Column(String(50))
    price = Column(Integer())

    reviews = relationship('Review', backref=backref('game'))
    # created_at=Column(datetime)
    # updated_at=Column(datetime)

    def __repr__(self):
        return f'Game(id={self.id},' +\
            f'title={self.title},' + \
            f'platform={self.platform})'


class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String(100))
    game_id = Column(Integer(), ForeignKey('games.id'))
#     created_at=Column(datetime)
#     updated_at=Column(datetime)

    def __repr__(self):
        return f'Review(id={self.id},' + \
            f'score={self.score},' + \
            f'game_id={self.game_id})'