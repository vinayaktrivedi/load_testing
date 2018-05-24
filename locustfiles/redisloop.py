import gevent.monkey
gevent.monkey.patch_all()
import time
import redis
from locust import Locust, events
from locust.core import TaskSet, task
from random import randint

class RedisClient(object):
    def __init__(self, host="localhost", port=6379):
        self.rc = redis.StrictRedis(host=host, port=port)

    def query(self, key, command='GET'):
        result = None
        start_time = time.time()
        for i in range(1000):
            result=self.rc.get(key)
        total_time = int((time.time() - start_time) *1000000)
        if not result:
            result = ''
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception="Error")
        else:
            length = len(result)
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result
class RedisLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(RedisLocust, self).__init__(*args, **kwargs)
        self.client = RedisClient()
        self.key='key2'
        self.value='value2'

class RedisLua(RedisLocust):
    # host = "http://127.0.0.1:8877/"
    min_wait = 100
    max_wait = 100

    class task_set(TaskSet):
        @task(1)
        def get_time(self):
            self.client.query('key1')


