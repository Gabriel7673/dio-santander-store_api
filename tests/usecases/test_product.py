from typing import List
from uuid import UUID

import pytest

from dio_santander_store_api.core.exceptions import NotFoundException
from dio_santander_store_api.schemas.product import ProductOut, ProductUpdateOut
from dio_santander_store_api.usecases.product import product_usecase


async def test_usecase_create_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro Max"


# async def test_usecase_get_return_success(product_id):
#     # Checar banco de dados se o produto foi criado
#     result = await product_usecase.get(id=product_id)

#     assert isinstance(result, ProductOut)
#     assert result.name == "Iphone 14 pro Max"


async def test_usecase_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("00000000-0000-0000-0000-000000000000"))

    assert (
        err.value.message
        == "Product not found with id: 00000000-0000-0000-0000-000000000000"
    )


async def test_usecase_query_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)


async def test_usecase_update_return_success(product_id, product_up):
    product_up.price = 7.500
    result = await product_usecase.update(id=product_id, body=product_up)

    assert isinstance(result, ProductUpdateOut)
