from decouple import config
from rq import Worker, Queue, Connection
from redis import Redis
"""
This worker does not work in windows, because
windows does not support fork() operation.
However since the worker can run separate
I created a docker image for that in a separate project
"""

redis_conn = Redis(
  host=config("REDIS_HOSTNAME"),
  port=config("REDIS_PORT"),
  password=config("REDIS_PASSWORD"))

# Create a worker and connect it to the default queue
with Connection(redis_conn):
    worker = Worker(Queue('default'))
    #Run the worker
    worker.work()