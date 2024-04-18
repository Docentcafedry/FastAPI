from . import crud
from fastapi import APIRouter, Depends, status
from core.models.db_helper import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.products.schemas import (
    ProductBase,
    ProductEntire,
    CreateProduct,
    PartialUpdateProduct,
)

from api_v1.products.dependencies import get_product


router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=list[ProductBase], status_code=status.HTTP_200_OK)
async def get_products(
    session: AsyncSession = Depends(db_helper.sessionmaker_dependency),
):
    return await crud.get_products(session=session)


@router.post("/", response_model=ProductBase, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: CreateProduct,
    session: AsyncSession = Depends(db_helper.sessionmaker_dependency),
):
    return await crud.create_product(session=session, product=product)


@router.get(
    "/{product_id}", response_model=ProductEntire, status_code=status.HTTP_200_OK
)
async def get_product(
    product: ProductEntire | None = Depends(get_product),
    session: AsyncSession = Depends(db_helper.sessionmaker_dependency),
):
    return product


@router.put("/{product_id}", response_model=ProductBase, status_code=status.HTTP_200_OK)
async def update_product_entire(
    updated_product: CreateProduct,
    product: ProductEntire | None = Depends(get_product),
    session: AsyncSession = Depends(db_helper.sessionmaker_dependency),
):
    return await crud.update_product(
        session=session, product=product, updated_product=updated_product
    )


@router.patch(
    "/{product_id}", response_model=ProductBase, status_code=status.HTTP_200_OK
)
async def update_product_partial(
    updated_product: PartialUpdateProduct,
    product: ProductEntire | None = Depends(get_product),
    session: AsyncSession = Depends(db_helper.sessionmaker_dependency),
):
    return await crud.update_product_partial(
        session=session, product=product, updated_product=updated_product
    )


@router.delete("/{product_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_product(
    product: ProductEntire | None = Depends(get_product),
    session: AsyncSession = Depends(db_helper.sessionmaker_dependency),
):
    await crud.delete_product(session=session, product_id=product.id)

    return {"deleted": "success"}
