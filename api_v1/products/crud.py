from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.products.schemas import (
    ProductBase,
    CreateProduct,
    ProductEntire,
    PartialUpdateProduct,
)
from core.models.product import Product


async def get_products(session: AsyncSession) -> list[ProductBase]:
    stmt = select(Product).order_by(Product.id)
    products = await session.scalars(stmt)
    return list(products.all())


async def get_product(session: AsyncSession, product_id: int) -> ProductBase:
    product = await session.query(Product).get(product_id)
    return product


async def create_product(session: AsyncSession, product: CreateProduct) -> ProductBase:
    product = Product(**product.model_dump())
    session.add(product)
    await session.commit()
    return product


async def update_product(
    session: AsyncSession, product: ProductEntire, updated_product: CreateProduct
) -> ProductBase:
    for key, value in updated_product.model_dump().items():
        setattr(product, key, value)
    await session.commit()
    return product


async def update_product_partial(
    session: AsyncSession, product: ProductBase, updated_product: PartialUpdateProduct
) -> ProductBase:
    for key, value in updated_product.model_dump(exclude_none=True).items():
        setattr(product, key, value)
    await session.commit()
    return product


async def delete_product(session: AsyncSession, product_id: int) -> None:
    stmt = delete(Product).where(Product.id == product_id)
    await session.execute(stmt)
    await session.commit()
