# EBANX Challenge - Startup Instructions

## Install dependencies
pip install -r requirements.txt

## Run the API (Uvicorn)
```powershell
# Terminal 1: start development server
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# If exposing via ngrok (recommended host 0.0.0.0)
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Expose with ngrok
```powershell
# Authenticate ngrok (run once)
ngrok authtoken <YOUR_NGROK_TOKEN>

# Terminal 2: create an HTTP tunnel to port 8000
ngrok http 8000
```