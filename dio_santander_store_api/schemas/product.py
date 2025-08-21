from decimal import Decimal
from typing import Annotated, Optional

from pydantic import AfterValidator, Field

from dio_santander_store_api.schemas.base import BaseSchemaMixin, OutSchema
from dio_santander_store_api.utils.converters import convert_decimal_128


class ProductBase(BaseSchemaMixin):
    name: str = Field(..., description="Name of the product")
    quantity: int = Field(..., description="Quantity of the product in stock")
    price: Decimal = Field(..., description="Price of the product")
    status: bool = Field(..., description="Status of the product, True if available")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn, OutSchema):
    ...


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(BaseSchemaMixin):
    quantity: Optional[int] = Field(
        None, description="Quantity of the product in stock"
    )
    price: Optional[Decimal_] = Field(None, description="Price of the product")
    status: Optional[bool] = Field(
        None, description="Status of the product, True if available"
    )


class ProductUpdateOut(ProductOut):
    ...
