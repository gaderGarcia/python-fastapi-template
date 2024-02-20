import random
#rule.py
#We are going to use an approach to import from github directly
def calculate_score(customer:str):
    #Dummy operation to provide an score between 0-10
    #based on the length of the customer
    lenght = len(customer)
    random_score=random.randrange(21)
    score = random_score - lenght
    if score < 0:
        return 0
    return score

def report_success(job, connection, result,*args, **kwargs):
    print(f"SUCCESS JOB, The value is: {result}")
    
def report_failure(job, connection, type, value, traceback):
    print(f"Job Failed due to: {traceback}")