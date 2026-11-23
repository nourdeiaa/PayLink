from fastapi import FastAPI

app = FastAPI(title="PayLink API")

@app.get("/")
def home():
    return {"message": "PayLink application is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}