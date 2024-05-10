from libgravatar import Gravatar
from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas import UserModel


async def get_user_by_email(email: str, db: Session) -> User:
    """
    Retrieve a user by their email address from the database.

    Args:
        email (str): The email address of the user to retrieve.
        db (Session): The SQLAlchemy session for database interaction.

    Returns:
        User: The user object if found, otherwise None.
    """
    return db.query(User).filter(User.email == email).first()


async def create_user(body: UserModel, db: Session) -> User:
    """
    Create a new user in the database and fetch a Gravatar image if available.

    Args:
        body (UserModel): The user data transfer object containing
                          user details.
        db (Session): The SQLAlchemy session for database interaction.

    Returns:
        User: The newly created user object with all details.
    """
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        print(e)
    new_user = User(**body.dict(), avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: Session) -> None:
    """
    Update the refresh token for a user in the database.

    Args:
        user (User): The user object whose token is to be updated.
        token (str | None): The new refresh token to be saved.
                            If None, it will clear the existing token.
        db (Session): The SQLAlchemy session for database interaction.
    """
    user.refresh_token = token
    db.commit()
