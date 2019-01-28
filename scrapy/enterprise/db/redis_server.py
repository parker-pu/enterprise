# coding=utf-8
"""
这个类的作用是操作 redis
"""
import json
import logging
import redis


class RedisServer(object):
    def __init__(self, **redis_kwargs):
        self.redis_kwargs = redis_kwargs
        self.logger = logging.getLogger("RedisServer")

    @property
    def conn(self):
        """ 这个函数的作用是用来连接Redis数据库
        :return:
        """
        if isinstance(self.redis_kwargs, dict):
            pass
        else:
            return

        for _ in range(10):
            try:
                return redis.StrictRedis(connection_pool=redis.ConnectionPool(
                    host=self.redis_kwargs.get('host')
                    , port=self.redis_kwargs.get('port')
                    , db=self.redis_kwargs.get('db')
                    , password=self.redis_kwargs.get('password')
                )).pipeline
            except Exception as e:
                self.logger.error(e)
        return None

    def add_data(self, key, values, add_type='set'):
        if bool(values) is False:
            return

        # 数据存入redis
        with self.conn() as pipe:
            for _ in range(10):
                try:
                    # 监听一个 key
                    pipe.watch(key)

                    # 事物开始
                    pipe.multi()
                    if add_type in ['set']:
                        pipe.set(name=key, value=json.dumps(values))
                    result = pipe.execute()
                    return result
                except Exception as e:
                    self.logger.error(e)
                finally:
                    # 重试直到 key 不被其它客户端影响
                    pipe.reset()

    def get_key(self, key=None):
        """ 用来处理单一的key的获取 """
        with self.conn() as pipe:
            for _ in range(10):
                try:
                    # 监听一个 key
                    pipe.watch(key)

                    # 事物开始
                    pipe.multi()
                    pipe.get(name=key)
                    result = pipe.execute()
                    return result
                except Exception as e:
                    self.logger.error(e)
                finally:
                    # 重试直到 key 不被其它客户端影响
                    pipe.reset()

    def append(self,):
        pass

    def get_hash_table(self):
        """ 用来处理 hash 表的数据 """
        pass
