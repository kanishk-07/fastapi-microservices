from .database import redis
from .models import Product
import time

key = 'payment_made'
group = 'inventory-group'

try:
    redis.xgroup_create(key, group)
except Exception as e:
    print(str(e))

while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)
        if results!=[]:
            for result in results:
                obj = result[1][0][1]
                product = Product.get(obj['product_id'])
                print(product)
                try:
                    product.quantity = product.quantity - int(obj['quantity'])
                    product.save()
                except:
                    redis.xadd('refund_order', obj, '*')
    except Exception as e:
        print(str(e))
    time.sleep(1)