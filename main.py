from typing import Union
from core import models
from core.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
from router import authentication, profile

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(profile.router)


if __name__ == "__main__":
    uvicorn.run(app, port=5000, host="0.0.0.0")


