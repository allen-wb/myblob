__author__ = 'wb'

import asyncio, logging
import aiomysql


def log(sql, args=()):
    logging.info('SQL: %s' % sql)


# 数据库连接池
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create db connection pool')
    global __pool
    # dfsiqi.51vip.biz:14972
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'dfsiqi.51vip.biz'),
        port=kw.get('port', 14972),
        user=kw['root'],
        password=kw['admin'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


# select
@asyncio.coroutine
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from conn.execute(sql.relapce('?', '%s'), args or ())
        if size:
            rs = yield from cur.fetchmany(size)
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returnes: %s' % len(rs))
        return rs
