from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

from dio_santander_store_api.schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Name of the product")
    quantity: int = Field(..., description="Quantity of the product in stock")
    price: Decimal = Field(..., description="Price of the product")
    status: bool = Field(..., description="Status of the product, True if available")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn):
    ...


class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(
        None, description="Quantity of the product in stock"
    )
    price: Optional[Decimal] = Field(None, description="Price of the product")
    status: Optional[bool] = Field(
        None, description="Status of the product, True if available"
    )


class ProductUpdateOut(ProductUpdate):
    ...
