from dio_santander_store_api.models.base import CreateBaseModel
from dio_santander_store_api.schemas.product import ProductIn


class ProductModel(CreateBaseModel, ProductIn):
    ...
