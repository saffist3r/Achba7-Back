from sqlalchemy.orm import Session

from . import models, schemas


# Users Related CRUD

# Read


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# Create


def create_user(db: Session, user: schemas.User):
    db_user = models.User(id='', password=user.password, name=user.name, surname=user.surname, photo=user.photo,
                          fonction=user.fonction,date_naissance=user.date_naissance, email=user.email,
                          telephone=user.telephone, city=user.city, country=user.country)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Update


# Delete

# Observations Related CRUD


# Read


def get_observations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Observation).offset(skip).limit(limit).all()


def get_observation_by_user(db: Session, user_id: str):
    return db.query(models.Observation).filter(models.Observation.id_user == user_id)


# Create


# Update


# Delete
# Animals Related CRUD


# Read


def get_animals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Animal).offset(skip).limit(limit).all()


def get_animal_by_id(db: Session, animal_id: str):
    return db.query(models.Animal).filter(models.Animal.id == animal_id).first()


# Create


# Update


# Delete
# Logs Related CRUD


# Read


def get_token(db: Session, user_id: str):
    return db.query(models.Logs).filter(models.Logs.user == user_id).first()


# Create


# Update


# Delete
# Alert_type Related CRUD


# Read


def get_alert_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AlertType).offset(skip).limit(limit).all()


# Create


# Update


# Delete
# Animal_Type Related CRUD


# Read


def get_animal_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AnimalType).offset(skip).limit(limit).all()


# Create


# Update


# Delete
# APP Related CRUD


# Read


def get_app(db: Session):
    return db.query(models.ApplicationInfo).first()
# Create


# Update


# Delete
