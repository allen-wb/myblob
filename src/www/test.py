from src.www.modles import User, Blog, Comment
import time, asyncio
from src.www.orm import create_pool


loop = asyncio.get_event_loop()


@asyncio.coroutine
def test_insert():
    yield from create_pool(loop)
    u = User(name='wb', email='test1@example.com', password='123456', image='about:blank', created_at=time.time())
    yield from u.save()


loop.run_until_complete(test_insert())
