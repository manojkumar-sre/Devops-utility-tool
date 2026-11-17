from fastapi import FastAPI
from routers import metrics, aws

app = FastAPI(
    title = "internal DevOps utilities API",
    description = "Internal utilities API for the system metrics, Aws usages, and log analysis",
    version = "1.2.0",
    docs_url = "/docs",
    redoc_url = "/redoc",

)

@app.get("/")

def hello():
    """
    this is a hello API, just for testing
    """
    return {"message": "hello Dosto, this is internal utility tool"}

app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")
