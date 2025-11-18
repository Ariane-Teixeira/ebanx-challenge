from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import PlainTextResponse
from app.models import Event
from app.services import reset, get_balance, deposit, withdraw, transfer

app = FastAPI()

@app.get("/")
def root():
    return {"message": "EBANX Banking API is running"}

@app.post("/reset")
def reset_state():
    reset()
    return Response(content="OK", status_code=200, media_type="text/plain")

@app.get("/balance")
def balance(account_id: str):
    balance = get_balance(account_id)
    if balance is None:
        return Response(content="0", status_code=404, media_type="text/plain")
    return balance

@app.post("/event", status_code=201)
def event_handler(event: Event):
    if event.type == "deposit":
        result = deposit(event.destination, event.amount)
        return {"destination": result}

    elif event.type == "withdraw":
        result = withdraw(event.origin, event.amount)
        if result is None:
            return Response(content="0", status_code=404, media_type="text/plain")
        return {"origin": result}

    elif event.type == "transfer":
        result = transfer(event.origin, event.destination, event.amount)
        if result is None:
            return Response(content="0", status_code=404, media_type="text/plain")
        return result

    else:
        raise HTTPException(status_code=400, detail="Invalid event type")