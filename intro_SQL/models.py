import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///projects.sqlite")
Base = declarative_base()


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    price = Column("price", Float)
    created_date = Column("created_date", DateTime, default=datetime.datetime.now(datetime.timezone.utc))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"


Base.metadata.create_all(engine)