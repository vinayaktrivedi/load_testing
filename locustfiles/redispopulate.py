import redis
client=redis.StrictRedis(host='127.0.0.1',port='6379')
for i in range(100000):
	key='key'+str(i)
	value='value'+str(i)
	client.set(key,value)

