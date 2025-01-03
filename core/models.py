from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from datetime import datetime
from .database import Base

timeFormat = datetime.now().strftime("%Y-%m-%d %H:%M")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    created = Column(String, default=timeFormat)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    profile = relationship("Profile", back_populates="user")

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    created = Column(String, default=timeFormat)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    profile_image = Column(String(500))
    username = Column(String(200), nullable=True)
    location = Column(String(200), nullable=True)
    short_intro = Column(String(200), nullable=True)
    bio = Column(String(2000), nullable=True)
    social_github = Column(String(200), nullable=True)
    social_twitter = Column(String(200), nullable=True)
    social_linkedin = Column(String(200), nullable=True)
    social_youtube = Column(String(200), nullable=True)
    social_website = Column(String(200), nullable=True)
    is_active = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="profile")
    # project = relationship("Project", back_populates="owner")
    # skill = relationship("Skill", back_populates="owner")
    # review = relationship("Review", back_populates="owner")