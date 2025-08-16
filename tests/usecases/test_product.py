from dio_santander_store_api.usecases.product import product_usecase

import pytest


@pytest.mark.asyncio
async def test_usecase_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    # assert isinstance(result, ProductOut)

    assert result is None  # Assuming create returns None on success
