from pydantic import BaseModel, Field, ConfigDict
from annotated_types import MinLen, MaxLen
from typing import Annotated


class ProductBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: Annotated[str, MinLen(2), MaxLen(15)]
    description: str
    price: int


class ProductEntire(ProductBase):
    id: int


class CreateProduct(ProductBase): ...


class PartialUpdateProduct(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(15)] | None = None
    description: str | None = None
    price: int | None = None
