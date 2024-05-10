from sqlalchemy import Column, Integer, String, Date, Text, func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    """
    Represents a contact entry in the database,
    storing personal and contact information.

    Attributes:
        id (Integer): The primary key for the contact
                      that is automatically generated.
        first_name (String): The contact's first name, a required field.
        last_name (String): The contact's last name, a required field.
        email (String): The contact's email address, must be unique.
        phone_number (String): The contact's phone number, an optional field.
        birthday (Date): The contact's date of birth, an optional field.
        additional_info (Text): Additional information or notes about
                                the contact, stored as text and is optional.
        created_at (DateTime): The timestamp when the contact was created,
                               defaults to the current time.
        updated_at (DateTime): The timestamp when the contact was last updated.
                               It updates automatically on modification
                               of the contact.
    """
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False, index=True)
    last_name = Column(String(50), nullable=False, index=True)
    email = Column(String(50), unique=True, index=True)
    phone_number = Column(String(15))
    birthday = Column(Date)
    additional_info = Column(Text)
    created_at = Column('created_at', DateTime, default=func.now())
    updated_at = Column(
        'updated_at', DateTime, default=func.now(), onupdate=func.now()
    )
