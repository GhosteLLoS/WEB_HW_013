from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.repository.contacts import (
    create_contact,
    get_contacts,
    get_contact_by_id,
    update_contact,
    delete_contact,
)
from src.schemas import ContactCreate, ContactRead

router = APIRouter()


@router.post("/contacts/", response_model=ContactRead)
async def create_new_contact(contact_data: ContactCreate, db: Session = Depends(get_db)):
    return create_contact(db, contact_data)


@router.get("/contacts/", response_model=list[ContactRead])
async def get_all_contacts(db: Session = Depends(get_db)):
    return get_contacts(db)


@router.get("/contacts/{contact_id}", response_model=ContactRead)
async def get_contact_by_id_endpoint(contact_id: int, db: Session = Depends(get_db)):
    contact = get_contact_by_id(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.put("/contacts/{contact_id}", response_model=ContactRead)
async def update_contact_endpoint(contact_id: int, contact_data: ContactCreate, db: Session = Depends(get_db)):
    contact = update_contact(db, contact_id, contact_data)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.delete("/contacts/{contact_id}", response_model=dict)
async def delete_contact_endpoint(contact_id: int, db: Session = Depends(get_db)):
    contact = get_contact_by_id(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return delete_contact(db, contact_id)
