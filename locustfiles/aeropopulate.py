import aerospike

# Configure the client
config = {
  'hosts': [ ('127.0.0.1', 3000) ]
}

# Create a client and connect it to the cluster
try:
  client = aerospike.client(config).connect()
except:
  import sys
  print("failed to connect to the cluster with", config['hosts'])
  sys.exit(1)

# Records are addressable via a tuple of (namespace, set, key)
for i in range(100000):
  main_key='key'+str(i)
  key = ('test', 'demo', main_key)
  client.put(key, {
    'name': 'John Doe',
    'age': 32
  })
print('success')
# Close the connection to the Aerospike cluster
client.close()
