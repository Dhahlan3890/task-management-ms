from fastapi import FastAPI

app = FastAPI(
    title="User Service",
    description="Microservice for user management",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Hello Dhahlan from User Service 🚀"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}