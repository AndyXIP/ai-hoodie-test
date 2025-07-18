import os
import uuid
from fastapi import APIRouter
from fastapi.responses import FileResponse
from PIL import Image

router = APIRouter()

HOODIE_FOLDER = "generated_hoodies"

@router.get("/hoodies")
async def list_hoodies():
    # List all image filenames in hoodie folder
    files = os.listdir(HOODIE_FOLDER)
    images = [f"/hoodies/image/{file}" for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]
    return {"hoodies": images}

@router.get("/hoodies/image/{image_name}")
async def get_hoodie_image(image_name: str):
    image_path = os.path.join(HOODIE_FOLDER, image_name)
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type="image/png")
    return {"error": "Image not found"}, 404

def generate_new_hoodie_image():
    # Replace with your actual image generation logic
    img = Image.new("RGB", (200, 200), color="green")  # dummy green square

    # Save with unique filename
    filename = f"{uuid.uuid4()}.png"
    path = os.path.join(HOODIE_FOLDER, filename)
    img.save(path)
    return filename

@router.post("/hoodies/generate")
async def generate_hoodie():
    filename = generate_new_hoodie_image()
    return {"message": "New hoodie generated", "filename": filename, "url": f"/hoodies/image/{filename}"}
