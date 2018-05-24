from pymemcache.client import base
client=base.Client(('localhost',11210))
for i in range(100000):
  key='key'+str(i)
  value='value'+str(i)
  client.set(key,value)
print('success')
