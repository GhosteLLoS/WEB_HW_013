from sqlalchemy.orm import Session
from src.database.db import SessionLocal
from src.schemas import ContactCreate, ContactRead
from src.database.models import Contact


def create_contact(db: Session, contact_data: ContactCreate):

    contact = Contact(**contact_data.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


def get_contacts(db: Session):

    return db.query(Contact).all()


def get_contact_by_id(db: Session, contact_id: int):

    return db.query(Contact).filter(Contact.id == contact_id).first()


def update_contact(db: Session, contact_id: int, contact_data: ContactCreate):

    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        for key, value in contact_data.model_dump().items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)
    return contact


def delete_contact(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return {"message": "Contact deleted successfully"}
