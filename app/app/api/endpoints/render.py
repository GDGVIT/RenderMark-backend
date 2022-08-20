import json
import pathlib

from celery.result import AsyncResult
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from schemas.video import Video
from tasks.tasks import render_video_task

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
        "task_result": task_result.info,
    }
    return JSONResponse(result)


@router.get("/videos/{video_path}")
def get_video(video_path):
    try:
        return FileResponse(f"media/{video_path}")
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Video not found") from exc


@router.get("/templates")
def get_templates():
    with open(pathlib.Path(__file__).parent / "templates.json") as f:
        templates = json.loads(f.read())
        return JSONResponse(templates)


@router.get("/structures/{template_name}")
def get_template_structure(template_name):
    with open(pathlib.Path(__file__).parent / "structures.json") as f:
        structures = json.loads(f.read())
        return JSONResponse(structures[template_name])
