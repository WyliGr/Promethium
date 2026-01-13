import json
from typing import Union
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Promethium", version="1.0.0")

with open("data/PeriodicTableJSON.json", "r", encoding="utf-8") as file:
    elements_data = json.load(file) 

@app.get("/", tags=["Root"])
def welcome_root():
    return {"message": "Welcome to the Promethium API! Don't forget to visit /docs for API documentation."}


