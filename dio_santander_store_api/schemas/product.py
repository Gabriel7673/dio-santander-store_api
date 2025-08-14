from pydantic import Field

from dio_santander_store_api.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):
    name: str = Field(..., description="Name of the product")
    quantity: int = Field(..., description="Quantity of the product in stock")
    price: float = Field(..., description="Price of the product")
    status: bool = Field(..., description="Status of the product, True if available")
