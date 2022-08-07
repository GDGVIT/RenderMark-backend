from urllib.error import HTTPError
from uuid import uuid4

from celery.result import AsyncResult
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from schemas.video import Video
from tasks.tasks import render_video_task
from utils.render import render_video
from worker import celery

router = APIRouter()


@router.post("/render")
async def render(video: Video):
    task = render_video_task.delay(video.dict())
    return JSONResponse({"task_id": task.id})

    # def iterfile():
    #     with open(video_path, mode="rb") as file_like:
    #         yield from file_like

    # return StreamingResponse(iterfile(), media_type="video/mp4")

    # return FileResponse(video_path)


@router.get("/status/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return JSONResponse(result)


@router.get("/videos/{video_path}")
def get_video(video_path):
    if video_path:
        return FileResponse(f"media/{video_path}")
    raise HTTPException(status_code=404, detail="Video not found")
