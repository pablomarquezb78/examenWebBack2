from database import MONGOCRUD

crud = MONGOCRUD('Logs')

async def add_log(log):
    result = await crud.create_item(log)
    return result

async def get_logs(filter):
    if len(filter) == 0:
        result = await crud.get_collection()
    else:
        result = await crud.get_by_filter(filter, sort=(["timestamp", -1]))
    return result

async def get_log(id: str):
    result = await crud.get_id(id)
    return result
    
async def delete_log(id:str):
    result = await crud.delete_id(id)
    return result

async def update_log(id: str, data: dict):
    result = await crud.update_id(id, data)
    return result