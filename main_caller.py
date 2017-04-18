import redis
from func1 import *
redis_client_obj = redis.Redis(host = 'localhost', port = 6379, db = 0)
redis_client_obj.flushall()
for x in range(1,100):
	f.delay(x)