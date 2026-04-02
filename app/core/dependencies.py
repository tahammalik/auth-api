"""
    ------Check dependencies to validate jwt token ------

    1. step - decode payload(data) from jwt token and take specific data(sub,username)
    2. step -  check if any of this none or not if any one is none raise error
    then take data from jwt take to validate with pydantic(data validation)
    
    catch - if any changes with jwt by external like wrong token or key etc it shows InvalidTokenError.
    
    at last we validate user (is this usernam from token does exist?) for avoiding ghost user.
"""

from fastapi.params import Depends
from jwt import InvalidTokenError
from app.services.auth_service import find_user
from app.schemas.token import UserToken
from app.core.db import db_dependency
from fastapi import HTTPException,status
from typing import Annotated
from app.core.config import SecretConfig
import jwt
from app.core.exceptions import UserNotFoundError
from fastapi.security import OAuth2PasswordBearer

secrets = SecretConfig()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# check every request to make sure the valid user
async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)],db:db_dependency):
      credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials"
      )
    # decode jwt token and extract user information
      try:
        payload = jwt.decode(token,secrets.secret_key,algorithms=[secrets.algorithm])
        id = payload.get('sub')
        
        if id is None:
            raise credentials_exception
        
        token_data = UserToken(id=int(id))
      except InvalidTokenError:
          raise credentials_exception
      
      # validate user with data from token
      user = find_user(token_data.id,db=db)
      
      if not user:
          raise UserNotFoundError(message=f"user not found!")
      
      return user

