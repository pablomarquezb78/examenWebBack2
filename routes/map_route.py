from fastapi import APIRouter, HTTPException, Body, Query
from models.mapas_schema import mapasSchema
import item_logic.map as map_logic
from typing import Optional

router = APIRouter()

@router.post("/")
async def add_map(map: mapasSchema = Body(...)):
    try:
        result = await map_logic.add_map(map.model_dump())
        return result
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")  
    
@router.get("/")
async def get_maps(
    lat: Optional[float] = Query(None),
    lon: Optional[float] = Query(None),
    email: Optional[str] = Query(None),
    ):
        filter = {}
        if lat and lon:
            filter["lat"] = {"$gte": lat - 0.2, "$lte": lat + 0.2}
            filter["lon"] = {"$gte": lon - 0.2, "$lte": lon + 0.2}

        if email:
            filter["email"] = email

        result = await map_logic.get_maps(filter)
        return result
    
@router.get("/{id}")    
async def get_map(id: str):
    try:
        result = await map_logic.get_map(id)
        return result
    except Exception as e:
        print(f"Failed to retrieve user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve map") 
    
@router.delete("/{id}")
async def delete_map(id:str):
    try:
        result = await map_logic.delete_map(id)
        return result
    except Exception as e:
        print(f"Failed to delete user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete map") 
    
@router.put("/{id}")
async def update_map(id: str, map: mapasSchema = Body(...)):
    try:
        result = await map_logic.update_map(id,map.model_dump())
        return result
    except Exception as e:
        print(f"Failed to update user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update map") 