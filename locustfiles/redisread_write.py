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
        try:
            result = self.rc.get(key)
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(result)
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result
    def write(self,key,value,command='write'):
        result=None
        start_time=time.time()
        try:
            result=self.rc.set(key,value)
            if not result:
                result=''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = 1
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result
class RedisLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(RedisLocust, self).__init__(*args, **kwargs)
        self.client = RedisClient()
        self.key='key1'
        self.value='value1'

class RedisLua(RedisLocust):
    # host = "http://127.0.0.1:8877/"
    min_wait = 100
    max_wait = 100

    class task_set(TaskSet):
        @task(2)
        def get_time(self):
            self.client.query('key1')
        @task(1)
        def write(self):
            self.client.write(self.key,self.value)
        @task(1)
        def get_key(self):
            var=str(randint(1,99999))
            self.key='key'+var
            self.value='value'+var

