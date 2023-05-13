from fastapi import APIRouter
from ..models import Order
from ..database import redis
from starlette.requests import Request
from fastapi.background import BackgroundTasks
import requests, time

router = APIRouter(
    prefix="/api/orders",
    tags=['Orders']
)


def fetch_order_based_on_pk(pk: str):
    product = Order.get(pk)
    return product


def make_payment(order: Order):
    time.sleep(5)
    order.status = 'completed'
    order.save() # to deduct items froom inventory we'll use redis streams
    redis.xadd('payment_made', order.dict(), '*')


@router.get('/')
def get_all_orders():
    primary_keys = Order.all_pks()
    return [fetch_order_based_on_pk(pk) for pk in primary_keys]


@router.get('/{pk}')
def get_order(pk: str):
    return fetch_order_based_on_pk(pk)


@router.post('/')
async def create_a_order(request: Request, background_tasks: BackgroundTasks): # we will be sending only product id & quantity
    body = await request.json()
    response = requests.get(f"http://localhost:8000/api/products/{body['product_id']}")
    product = response.json()
    order = Order(
        product_id = body['product_id'],
        quantity = body['quantity'],
        price = product['price'],
        fee = product['price']*0.2,
        total = product['price']*1.2,
        status = 'pending',
    )
    order.save()
    #make_payment(order)
    background_tasks.add_task(make_payment, order)
    return order