import gevent.monkey
gevent.monkey.patch_all()
import time
import aerospike
from locust import Locust, events
from locust.core import TaskSet, task


class AerospikeClient(object):
    def __init__(self):
        self.config = {'hosts': [ ('127.0.0.1', 3000) ]}
        self.client=aerospike.client(self.config).connect()
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


class RedisLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(RedisLocust, self).__init__(*args, **kwargs)
        self.client = AerospikeClient()


class RedisLua(RedisLocust):
    # host = "http://127.0.0.1:8877/"
    min_wait = 100
    max_wait = 100

    class task_set(TaskSet):
        @task(1)
        def get_time(self):
            self.key= ('test', 'demo', 'fooagain')
            self.client.query(self.key)
