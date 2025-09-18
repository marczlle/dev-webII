from fastapi import FastAPI, Query
from pydantic import BaseModel
import os

app = FastAPI()
CONTAINER = os.getenv("CONTAINER_NAME", "unknown")

class Operands(BaseModel):
    op1: float
    op2: float

@app.get("/mult")
def mult_get(op1: float = Query(...), op2: float = Query(...)):
    result = op1 * op2
    return {"op1": op1, "op2": op2, "result": result, "container": CONTAINER}

@app.post("/mult")
def mult_post(payload: Operands):
    result = payload.op1 * payload.op2
    return {"op1": payload.op1, "op2": payload.op2, "result": result, "container": CONTAINER}
