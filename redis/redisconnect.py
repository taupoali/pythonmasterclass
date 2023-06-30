import redis

r = redis.Redis(
    host='127.0.0.1',
    port=49154,
    password='redispw'
    )

r.set('foo', 'bar')
value = r.get('foo')
print(value)

# now lets retrieve a key value from a key that already exists in redi\s
customer = r.get('customer:1000')
print(customer)
