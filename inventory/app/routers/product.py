from fastapi import APIRouter
from ..models import Product

router = APIRouter(
    prefix="/api/products",
    tags=['Products']
)

def fetch_product_based_on_pk(pk: str):
    product = Product.get(pk)
    return product

@router.get('/')
def get_all_products():
    primary_keys = Product.all_pks()
    return [fetch_product_based_on_pk(pk) for pk in primary_keys]


@router.get('/{pk}')
def get_product(pk: str):
    return fetch_product_based_on_pk(pk)


@router.post('/')
def create_a_product(product: Product):
    return product.save()


@router.delete('/{pk}')
def delete_product(pk: str):
    return Product.delete(pk)