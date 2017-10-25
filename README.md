# test-queueing-celery-redis
A test repo for a glance on redis-celery queueing and broker system

## modules needed
1.	[Celery](http://docs.celeryproject.org/en/latest/index.html) can be installed by pip using 
		`$ pip install celery`
2.	[Redis](https://redis.io/download) broker system

### Go to step
1.	Start redis server by using the command 
		`$ redis-server`
2.	Open another terminal and run the command to start celery 
		`$ celery -A sample_function worker --loglevel=info`
3.	Run you main script in an another terminal window and see whether tasks are being queued and completed in celery window

## Resources
1.  [This](https://tests4geeks.com/python-celery-rabbitmq-tutorial/) quick on read on asynchronous task distribution using Celery and RabbitMQ gets you started real quick
