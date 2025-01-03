from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from core import models, database, schemas
from repository import authentication
from fastapi import Depends, status, APIRouter
from sqlalchemy.orm import Session

router = APIRouter(tags=["Authentication"])

# route for user registration
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(request: schemas.UserBase, db: Session = Depends(database.get_db)):
    return authentication.register(request, db)

# route for user login
@router.post("/login")
def login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    return authentication.login(request, db)


# route for user logout
@router.get("/logout")
async def logout(request: Request):
    response = RedirectResponse("/login", status_code=status.HTTP_302_FOUND)
    response.delete_cookie(key="access_token")
    return response