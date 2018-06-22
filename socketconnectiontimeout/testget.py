import threading
import time
import redis
exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.rc = redis.StrictRedis(unix_socket_path='/var/run/redis/redis.sock')
   def run(self):
      get_key(self.threadID,self.rc)

def get_key(threadID,conn):
   while (1):
      conn.get('key1')

# Create new threads
for i in range(100):
   myThread(i).start()

print "Exiting Main Thread"
