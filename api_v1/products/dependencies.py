from sqlalchemy import select
from fastapi import Depends, Path, HTTPException, status
from typing import Annotated
from api_v1.products.schemas import ProductBase, ProductEntire
from core.models.product import Product
from sqlalchemy.ext.asyncio import AsyncSession
from core.models.db_helper import db_helper


async def get_product(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.sessionmaker_dependency),
) -> Product:
    print(product_id)

    product = await session.get(Product, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There is no product with id {product_id}",
        )

    return product
