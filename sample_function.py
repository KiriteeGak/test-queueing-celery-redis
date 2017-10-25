from celery import Celery
app = Celery('sample_function', broker = "redis://")

def g(x):
	return x

@app.task
def f(x):
	return (g(x)*x)+2