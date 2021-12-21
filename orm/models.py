from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Fish(Base):
    __tablename__ = 'fish'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    month_northern = Column(String)
    month_southern = Column(String)
    time = Column(String)
    is_all_day = Column(Boolean)
    is_all_year = Column(Boolean)
    location = Column(String)
    rarity = Column(String)
    shadow = Column(String)
    price = Column(Integer)
    price_cj = Column(Integer)
    catch_phrase = Column(String)
    museum_phrase = Column(String)
    image_uri = Column(String)
    icon_uri = Column(String)
    months_available = relationship('FishMonthAvailability')

    def __repr__(self):
        return f'{self.name} | {self.price} | {[m.month for m in self.months_available]}'

class FishMonthAvailability(Base):
    __tablename__ = 'fish_month_availability'

    fish_id = Column(Integer, ForeignKey('fish.id'), primary_key=True)
    month = Column(Integer, primary_key=True)
