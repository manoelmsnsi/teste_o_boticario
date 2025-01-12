import sqlalchemy
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base


metadata = sqlalchemy.MetaData()
Base = declarative_base()

class Token(BaseModel):
    access_token: str
    token_type: str
    token_expire: str

class TokenData(BaseModel):
    username: str | None = None
