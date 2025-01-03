from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    is_active: Optional[bool]

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class ProfileBase(BaseModel):
    first_name: str
    last_name: str
    location: str
    short_intro: str
    bio: str
    social_github: str
    social_twitter: str
    social_linkedin: str
    social_youtube: str
    social_website: str