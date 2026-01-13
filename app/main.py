from fastapi import FastAPI
from routers import elements

app = FastAPI(title="Promethium", version="1.0.0")

app.include_router(elements.router)

@app.get("/", tags=["Root"])
def welcome_root():
    return {"message": "Welcome to the Promethium API! Visit /docs for documentation."}