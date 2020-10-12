import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379
    )

r.set('foo', 'bar')
value = r.get('foo')
print(value)

# now lets retrieve a key value from a key that already exists in redi\s
customer = r.get('customer:1000')
print(customer)
