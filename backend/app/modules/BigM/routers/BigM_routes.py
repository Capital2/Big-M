from fastapi import APIRouter
from ..controllers.BigM_controller import BigM_controller

router = APIRouter(
    tags=['BigM'],
    prefix='/BigM',
)

@router.post("/test")
# , response_model=Token
async def test():
    return BigM_controller.test_method()
