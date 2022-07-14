from fastapi import APIRouter

router = APIRouter()


@router.get("/render")
def render():
    return {"message": "rendered video"}
