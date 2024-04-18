from core.models.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String


class Product(Base):

    name: Mapped[str] = mapped_column(String(15))
    description: Mapped[str] = mapped_column(String(50))

    price: Mapped[int]

    def __repr__(self) -> str:
         return f"Product(id={self.id!r}, name={self.name!r}, price={self.price!r})"