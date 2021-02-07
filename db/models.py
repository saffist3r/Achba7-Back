from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    photo = Column(String)
    fonction = Column(String)
    date = Column(String)
    email = Column(String)
    telephone = Column(String)
    city = Column(String)
    country = Column(String)
    #observations = relationship("Observation", back_populates="owner")


class Observation(Base):
    __tablename__ = "observations"
    id = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer)
    alert_type = Column(String)
    animal = Column(Integer)
    longitude = Column(String)
    latitude = Column(String)
    description = Column(String)
    photo = Column(String)
    date = Column(String)
    #observations = relationship("User", back_populates="observations")


class Logs(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String)
    date = Column(String)
    user = Column(Integer)
    active = Column(Integer)


class AnimalType(Base):
    __tablename__ = "animal_type"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    photo = Column(String)


class Animal(Base):
    __tablename__ = "animals"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Integer)
    name = Column(String)
    photo = Column(String)


class AlertType(Base):
    __tablename__ = "alert_type"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    photo = Column(String)


class ApplicationInfo(Base):
    __tablename__ = "APP"
    name = Column(String, primary_key=True, index=True)
    logo = Column(String)
    description = Column(String)
    owner = Column(String)
    version = Column(String)



