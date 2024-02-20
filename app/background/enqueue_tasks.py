from redis import Redis
from decouple import config
from rq import Queue, Callback
#from ..tasks import rule #We are going to pull from my github repo
from rules import rule
import time

#Tell RQ what Redis connection to use
redis_conn = Redis(
  host=config("REDIS_HOSTNAME"),
  port=config("REDIS_PORT"),
  password=config("REDIS_PASSWORD"))

#Create a queue using the default queue name
# by default the name of the queu is 'default'
queue = Queue(connection=redis_conn)

def get_fraud_score(customer:str)->int:
    total = 0
    async_results = {}
    #
    for x in range(0,10):
        #Enqueue the calculate_square task with argument 5
        async_results[x] = queue.enqueue(rule.calculate_score,customer,on_success=Callback(rule.report_success))
    
    start_time = time.time()
    is_done= False
    while not is_done:
        print("Running process")
        is_done=True
        total = 0
        for x in range(0,10):
            result = async_results[x].result
            if result is not None:
                total+=result
            else:
                is_done=False
    print(f"TimeProcessing Jobs:{time.time()-start_time}")
    print(f"result:{total}")
    return total
