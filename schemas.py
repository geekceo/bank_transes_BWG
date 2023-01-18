from pydantic import BaseModel, Field, validator

class User(BaseModel):
    
    name: str = Field(...)
    balance: int = Field(default=0)
    
    
class Transaction(BaseModel):
    
    u_from: str = Field(...)
    u_to: str = Field(...)
    amount: int = Field(...)
    status: str = Field(default='New')