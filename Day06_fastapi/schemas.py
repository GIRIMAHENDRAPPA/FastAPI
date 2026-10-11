from pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    title: str
    
class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int
    class config:
        from_attributes = True
        
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    items: List[Item] = []
    class config:
        from_attributes = True