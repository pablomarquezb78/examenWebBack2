from fastapi import APIRouter, HTTPException, Body, Query
from models.eventos_schema import eventosSchema
import item_logic.event as event_logic
from typing import Optional

router = APIRouter()

@router.post("/")
async def add_event(evento: eventosSchema = Body(...)):
    try:
        result = await event_logic.add_event(evento.model_dump())
        return result
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")  
    
@router.get("/")
async def get_events(
    lat: Optional[float] = Query(None),
    lon: Optional[float] = Query(None),
    nombre: Optional[str] = Query(None),
    organizador: Optional[str] = Query(None),
    ):
        filter = {}
        if lat and lon:
            filter["lat"] = {"$gte": lat - 0.2, "$lte": lat + 0.2}
            filter["lon"] = {"$gte": lon - 0.2, "$lte": lon + 0.2}

        if nombre:
            filter["nombre"] = {"$regex": ".*{}.*".format(nombre), "$options": "i"}
        if organizador:
            filter["organizador"] = {"$regex": ".*{}.*".format(organizador), "$options": "i"}

        result = await event_logic.get_events(filter)
        return result
    
@router.get("/{id}")    
async def get_event(id: str):
    try:
        result = await event_logic.get_event(id)
        return result
    except Exception as e:
        print(f"Failed to retrieve user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve event") 
    
@router.delete("/{id}")
async def delete_event(id:str):
    try:
        result = await event_logic.delete_event(id)
        return result
    except Exception as e:
        print(f"Failed to delete user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete event") 
    
@router.put("/{id}")
async def update_event(id: str, evento: eventosSchema = Body(...)):
    try:
        result = await event_logic.update_event(id,evento.model_dump())
        return result
    except Exception as e:
        print(f"Failed to update user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update event") 