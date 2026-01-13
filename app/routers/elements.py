import json
import os
import random
from fastapi import APIRouter, HTTPException

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(BASE_DIR, "data", "PeriodicTableJSON.json")

with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)
    elements_list = data.get("elements", [])

router = APIRouter(
    prefix="/elements",
    tags=["Elements"]
)



@router.get("/")
def get_all_elements():
    return elements_list

@router.get("/{number}")
def get_element_by_number(number: int):
    element = next((e for e in elements_list if e["number"] == number), None)
    if not element:
        raise HTTPException(status_code=404, detail="Unknown element number")
    return element

@router.get("/symbol/{symbol}")
def get_element_by_symbol(symbol: str):
    element = next((e for e in elements_list if e["symbol"].lower() == symbol.lower()), None)
    if not element:
        raise HTTPException(status_code=404, detail="Unknown element symbol")
    return element

@router.get("/name/{name}")
def get_element_by_name(name: str):
    element = next((e for e in elements_list if e["name"].lower() == name.lower()), None)
    if not element:
        raise HTTPException(status_code=404, detail="Unknown element name")
    return element

@router.get("/wiki/nb/{number}")
def get_element_by_number(number: int):
    element = next((e for e in elements_list if e["number"] == number), None)
    if not element:
        raise HTTPException(status_code=404, detail="Unknown element number")
    return element.get("source")

@router.get("/wiki/{name}")
def get_element_by_name(name: str):
    element = next((e for e in elements_list if e["name"].lower() == name.lower()), None)
    if not element:
        raise HTTPException(status_code=404, detail="Unknown element name")
    return element.get("source")

@router.get("/stats/count")
def get_elements_count():
    return {"count": len(elements_list)}

