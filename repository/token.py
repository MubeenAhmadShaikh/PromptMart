from __future__ import annotations
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from core import schemas, models, database
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Request
from typing import Union

SECRET_KEY = "bf84907e092a545c4e0016231265fde1a734de1f66264f674d8eedb144d50de4"
ALGORITHM = "HS256"

# Creation of access token once creds are valid
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# To return the current users profile object
def get_user(username, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == username).first()
    user_profile = (
        db.query(models.Profile).filter(models.Profile.user_id == user.id).first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not Authorized"
        )
    return user_profile


# To verify the generated token
def verify_token(tokendata, credentials_exception, db):
    try:
        payload = jwt.decode(tokendata, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(username, db)
    if user is None:
        raise credentials_exception
    return user

