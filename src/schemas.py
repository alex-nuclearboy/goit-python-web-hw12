from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field


class ContactBase(BaseModel):
    """
    Base model for contact information,
    used as a foundation for other contact-related models.

    Attributes:
        first_name (str): The first name of the contact.
        last_name (str): The last name of the contact.
        email (str): The email address of the contact.
        phone_number (str): The contact's phone number.
        birthday (date): The birthday of the contact.
        additional_info (Optional[str]): Additional information about
                                         the contact, optional.
    """
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=50)
    phone_number: str = Field(max_length=15)
    birthday: date
    additional_info: Optional[str] = None


class ContactModel(ContactBase):
    """
    A model representing a contact, extending ContactBase
    without additional fields. This model is used for creating new contacts
    where all fields are required.
    """
    pass


class ContactUpdate(BaseModel):
    """
    A model for updating existing contacts. All fields are optional.

    Attributes are identical to ContactBase, but all are optional
    to allow for partial updates.
    """
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    email: Optional[str] = Field(None, max_length=50)
    phone_number: Optional[str] = Field(None, max_length=15)
    birthday: Optional[date] = None
    additional_info: Optional[str] = None


class ContactResponse(ContactBase):
    """
    A response model for contact information that extends ContactBase
    with additional fields.

    Attributes:
        id (int): The unique identifier for the contact.
        created_at (datetime): The date and time when the contact was
                               originally created in the system.
        updated_at (datetime): The date and time when the contact information
                               was last updated.
    """
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=10)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"