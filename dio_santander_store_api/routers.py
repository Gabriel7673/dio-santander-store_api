from fastapi import APIRouter

from dio_santander_store_api.controllers.product import router as product_router

api_router = APIRouter()
api_router.include_router(product_router, prefix="/products")
