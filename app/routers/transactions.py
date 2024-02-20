from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..background import enqueue_tasks

router = APIRouter()

class Transaction(BaseModel):
    customer:str
    score:int
    id:int
    # def __init__(self,name,age):
    #     self.name= name
    #     self.age=age

transactions = {
    0:Transaction(customer="ShoesX",score=100,id=0),
    1:Transaction(customer="ShoesX",score=100,id=1),
    2:Transaction(customer="ShoesX",score=100,id=2)
}

@router.get("/transactions")
async def get_transactions()->dict[int, Transaction]:
    return transactions

@router.get("/transactions/score")
async def get_score(customer:str)->dict[str, int]:
    score = enqueue_tasks.get_fraud_score(customer)
    return {"score":score}

@router.post("/transactions")
def add_transaction(trx:Transaction)->dict[str,Transaction]:
    if trx.id in transactions:
        raise HTTPException(status_code=400,detail=f"Transaction id: {trx.id} already exists.")

    transactions[trx.id]=trx
    return {"added":trx}