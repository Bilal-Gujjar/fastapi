from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ....core.security import authenticate_user, create_access_token
from ....schemas.user import Token

router = APIRouter()

@router.post("/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Add additional routes for registration, etc., if needed.
# from fastapi import APIRouter

# router = APIRouter()

# @router.get("/")
# def get_sales_data():
#     # Placeholder. This should return sales data.
#     return {"message": "Sales data"}

