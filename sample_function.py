from celery import Celery
app = Celery('func1', broker = "redis://")

def g(x):
	return x

@app.task
def f(x):
	return (g(x)*x)+2