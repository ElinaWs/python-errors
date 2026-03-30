from datetime import datetime

from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    created_at: datetime | None = None

    class Config:
        from_attributes = True #добавление Config