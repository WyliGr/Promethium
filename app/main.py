import json
from typing import Union
from fastapi import FastAPI, HTTPException

# Making JSON Data File Path Dynamic
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "data", "PeriodicTableJSON.json")

app = FastAPI(title="Promethium", version="1.0.0")

# Load JSON data
with open(json_path, "r", encoding="utf-8") as file:
    elements_data = json.load(file) 

# Root endpoint
@app.get("/", tags=["Root"])
def welcome_root():
    return {"message": "Welcome to the Promethium API! Don't forget to visit /docs for API documentation."}

