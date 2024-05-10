from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.schemas import ContactModel, ContactResponse, ContactUpdate
from src.repository import contacts as repository_contacts
from datetime import date

router = APIRouter(prefix='/contacts')


@router.get("/birthdays", response_model=List[ContactResponse])
async def get_upcoming_birthdays(db: Session = Depends(get_db)):
    today = date.today()
    upcoming_birthdays = (
        await repository_contacts.get_upcoming_birthdays(db, today)
    )
    return upcoming_birthdays


@router.get("/", response_model=List[ContactResponse])
async def read_contacts(skip: int = 0,
                        limit: int = 100,
                        search: str = None,
                        db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(skip, limit, search, db)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    return await repository_contacts.create_contact(body, db)


@router.patch("/{contact_id}", response_model=ContactResponse)
async def update_contact(contact_id: int,
                         body: ContactUpdate,
                         db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse)
async def remove_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.remove_contact(contact_id, db)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact
