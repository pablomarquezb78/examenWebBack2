from item_logic.crud_inheritance.map_crud import MAPCRUD

crud = MAPCRUD()

async def add_map(event):
    result = await crud.create_item(event)
    return result

async def get_maps(filter):
    if len(filter)==0:
        result = await crud.get_collection()
    else: 
        result = await crud.get_by_filter(filter, sort=(["timestamp", -1]))
    return result

async def get_map(id: str):
    result = await crud.get_id(id)
    return result
    
async def delete_map(id:str):
    result = await crud.delete_id(id)
    return result

async def update_map(id: str, data: dict):
    result = await crud.update_id(id, data)
    return result