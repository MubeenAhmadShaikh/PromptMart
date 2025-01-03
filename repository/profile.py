from sqlalchemy.orm import Session
from core import schemas, database, models
from fastapi import FastAPI, Depends

# To create basic info of profile
def create_profile(
    username, first_name, last_name, db: Session = Depends(database.get_db)
):
    user = db.query(models.User).filter(models.User.email == username).first()
    create_profile = models.Profile(
        first_name=first_name,
        last_name=last_name,
        username=username,
        is_active=True,
        user_id=user.id,
    )
    db.add(create_profile)
    db.commit()
    db.refresh(create_profile)
    return True