from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, StreamingResponse
from schemas.video import Video
from utils.render import render_video

router = APIRouter()


@router.post("/render")
async def render(video: Video):
    video_path = render_video(video)

    def iterfile():
        with open(video_path, mode="rb") as file_like:
            yield from file_like

    return StreamingResponse(iterfile(), media_type="video/mp4")

    # return FileResponse(video_path)
