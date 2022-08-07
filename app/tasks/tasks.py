from utils.render import render_video
from worker import celery


@celery.task
def render_video_task(video):
    return render_video(video)
