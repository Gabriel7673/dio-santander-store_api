from decimal import Decimal
from typing import Annotated, Optional

from bson import Decimal128
from pydantic import AfterValidator, BaseModel, Field

from dio_santander_store_api.schemas.base import BaseSchemaMixin, OutMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Name of the product")
    quantity: int = Field(..., description="Quantity of the product in stock")
    price: Decimal = Field(..., description="Price of the product")
    status: bool = Field(..., description="Status of the product, True if available")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutMixin):
    ...


def convert_decimal_128(v):
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(
        None, description="Quantity of the product in stock"
    )
    price: Optional[Decimal_] = Field(None, description="Price of the product")
    status: Optional[bool] = Field(
        None, description="Status of the product, True if available"
    )


class ProductUpdateOut(ProductUpdate, OutMixin):
    ...
