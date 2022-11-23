from fastapi import APIRouter
from ..controllers.BigM_controller import BigM_controller

router = APIRouter(
    tags=['BigM'],
    prefix='/BigM',
)

@router.post("/process")
async def process(req_body: dict):
    formatted_data = BigM_controller.format_data(req_body)
    iterations = BigM_controller.perform_BigM(formatted_data)
    return iterations
