import time
from fastapi import FastAPI, Request
from .routers import transactions

app = FastAPI()

#include routers
app.include_router(transactions.router)

@app.middleware("http")
async def intercept_request(request: Request, call_next):
    start_time=time.time()
    response=await call_next(request)
    process_time= time.time()-start_time
    print(f"Execution time:{process_time}")
    response.headers["X-Process-Time"]=str(process_time)
    return response

@app.get("/", status_code=200)
async def health_check():
    return {"status":"OK"}