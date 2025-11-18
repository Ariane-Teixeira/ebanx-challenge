accounts = {}

def reset():
    accounts.clear()

def get_balance(account_id: str):
    if account_id not in accounts:
        return None
    return accounts[account_id]

def deposit(destination: str, amount: int):
    if destination not in accounts:
        accounts[destination] = 0
    accounts[destination] += amount
    return {"id": destination, "balance": accounts[destination]}

def withdraw(origin: str, amount: int):
    if origin not in accounts:
        return None
    accounts[origin] -= amount
    return {"id": origin, "balance": accounts[origin]}

def transfer(origin: str, destination: str, amount: int):
    if origin not in accounts:
        return None
    if destination not in accounts:
        accounts[destination] = 0
    accounts[origin] -= amount
    accounts[destination] += amount
    return {
        "origin": {"id": origin, "balance": accounts[origin]},
        "destination": {"id": destination, "balance": accounts[destination]}
    }