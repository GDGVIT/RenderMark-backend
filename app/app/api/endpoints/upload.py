import uuid

import cloudinary
import cloudinary.api
import cloudinary.uploader
from fastapi import APIRouter, Request, Response

router = APIRouter()


@router.route("/FileUploader", methods=["GET", "POST"])
async def file_upload(request: Request):
    file = await request.body()
    # with open(f"file{guess_extension(request.content_type)}", "wb") as blob:
    #     blob.write(file)
    file_name = str(uuid.uuid4())
    cloudinary.uploader.upload(
        file,
        public_id=file_name,
        unique_filename=False,
        overwrite=True,
    )
    src_url = cloudinary.CloudinaryImage(file_name).build_url()
    return Response(src_url)
