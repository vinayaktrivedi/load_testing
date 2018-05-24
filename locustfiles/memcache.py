from pymemcache.client import base
import gevent.monkey
gevent.monkey.patch_all()
import time
from locust import Locust, events
from locust.core import TaskSet, task
from random import randint
class MemcacheClient(object):
    def __init__(self):
        self.client= base.Client(('localhost', 11210))
    def query(self,key,command='GET'):
        result = None
        start_time = time.time()
        try:
            result = self.client.get(key)
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


class MemcacheLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(MemcacheLocust, self).__init__(*args, **kwargs)
        self.client = MemcacheClient()


class MemcacheLua(MemcacheLocust):
    # host = "http://127.0.0.1:8877/"
    min_wait = 100
    max_wait = 100

    class task_set(TaskSet):
        @task(1)
        def get_time(self):
            key= 'key'+str(randint(1,9999))
            self.client.query(key)
