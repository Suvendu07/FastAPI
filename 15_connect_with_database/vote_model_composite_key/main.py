from fastapi import FastAPI
from .database import Base, engine
from .votes import router2
from .routes import router


Base.metadata.create_all(bind = engine)


app = FastAPI()

app.include_router(router2)
app.include_router(router)