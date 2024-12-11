from item_logic.crud_inheritance.event_crud import EVENTCRUD

crud = EVENTCRUD()

async def add_event(event):
    result = await crud.create_item(event)
    return result

async def get_events(filter):
    if len(filter)==0:
        result = await crud.get_collection()
    else: 
        result = await crud.get_by_filter(filter, sort=(["timestamp", -1]))
    return result

async def get_event(id: str):
    result = await crud.get_id(id)
    return result
    
async def delete_event(id:str):
    result = await crud.delete_id(id)
    return result

async def update_event(id: str, data: dict):
    result = await crud.update_id(id, data)
    return result