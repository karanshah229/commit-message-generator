from pydantic import BaseModel
from typing import Optional

class Ticket(BaseModel):
    id: Optional[int]
    title: str
    description: str
    status: str

class TicketCreate(BaseModel):
    title: str
    description: Optional[str] = ""
    status: str

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
