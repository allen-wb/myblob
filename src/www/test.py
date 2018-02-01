from src.www.orm import create_pool
import asyncio
from src.www.modles import User, Comment, Blog
import time


loop = asyncio.get_event_loop()


@asyncio.coroutine
def test():
    yield from create_pool(loop=loop, host='192.168.1.51', port=3306, user='root', password='admin', db='wb_test')

    u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank', id='4564', created_at=time.time())
    yield from u.save()


loop.run_until_complete(test())






