from fastapi import APIRouter, HTTPException, Body, Query
from models.logs_schema import logSchema
import item_logic.log as log_logic
from typing import Optional

router = APIRouter()

@router.post("/")
async def add_log(log: logSchema = Body(...)):
    try:
        result = await log_logic.add_log(log.model_dump())
        return result
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")  
    
@router.get("/")
async def get_logs(filter_user: Optional[str] = Query(None)):
    try:
        filter = {}

        if filter_user:
            filter["email"] = filter_user

        result = await log_logic.get_logs(filter)
        return result
    except Exception  as e:
        print(f"Failed to retrieve users: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve logs") 
    
@router.get("/{id}")    
async def get_log(id: str):
    try:
        result = await log_logic.get_log(id)
        return result
    except Exception as e:
        print(f"Failed to retrieve user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve log") 
    
@router.delete("/{id}")
async def delete_log(id:str):
    try:
        result = await log_logic.delete_log(id)
        return result
    except Exception as e:
        print(f"Failed to delete user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete log") 
    
@router.put("/{id}")
async def update_log(id: str, log: logSchema = Body(...)):
    try:
        result = await log_logic.update_log(id,log.model_dump())
        return result
    except Exception as e:
        print(f"Failed to update user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update log") 