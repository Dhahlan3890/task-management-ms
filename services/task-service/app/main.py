from fastapi import FastAPI

app = FastAPI(title="Task Service")

@app.get("/")
async def root():
    return {"message": "Hello from Task Service! 🚀"}

@app.get("/health")
async def health():
    return {"status": "healthy"}