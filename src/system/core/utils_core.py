
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UtilsCore():    
    def __init__(self) -> None:
        pass

    def get_password_hash(self,password):
        return pwd_context.hash(password) 