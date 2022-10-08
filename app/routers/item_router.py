from fastapi import APIRouter
from app.services import item_services

router = APIRouter(
    prefix="/items"
)

@router.get("/{item_id}")
async def get_item(item_id):
    return item_services.get_item_by_id(item_id)