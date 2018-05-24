from pymemcache.client import base
client=base.Client(('localhost',11210))
client.set('test','pharmeasy')
print(client.get('test'))
