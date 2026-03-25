from passlib.context import CryptContext



# it is use for to convert the normal password to hasing password
pwd_context = CryptContext(schemes=["argon2"], deprecated = "auto")



def hash(password : str):
    return pwd_context.hash(password)



def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)