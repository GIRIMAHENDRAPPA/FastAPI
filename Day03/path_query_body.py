from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional

app = FastAPI()

class UserUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, example="John Doe")
    email: EmailStr = Field(..., example="john@test.com")
    age: Optional[int] = Field(None, gt=0, le=120, description="Age must be >0 and <120")

    @field_validator('n
    def name_must_not_have_number(cls, v):
        if any(char.isdigit() for char in v):
            raise ValueError('Name should not contain numbers')
        return v

@app.put("/{user_id}")
def update_user(
    user_id: int = Path(..., gt=0, description="User ID must be >0"),
    q: Optional[str] = Query(None, min_length=2, max_length=50, example="search"),
    user: UserUpdate =...
):
    return {
        "path_id": user_id,
        "query_q": q,
        "updated_data": user.model_dump(),
        "message": f"User {user_id} updated"
    }