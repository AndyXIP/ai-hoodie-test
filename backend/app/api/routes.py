import os
import uuid
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from PIL import Image
import json

router = APIRouter()

HOODIE_FOLDER = "data/images"
DB_PATH = "data/hoodies.json"

def load_hoodies():
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_hoodies(hoodies):
    with open(DB_PATH, "w") as f:
        json.dump(hoodies, f, indent=2)

@router.get("/hoodies")
async def list_hoodies():
    return load_hoodies()

@router.get("/hoodies/image/{category}/{image_name}")
async def get_hoodie_image(category: str, image_name: str):
    if category not in ("generated", "original"):
        raise HTTPException(status_code=400, detail="Invalid category")

    hoodies = load_hoodies()
    print(category)
    # Check if image exists in metadata (exact match on category + image)
    if not any(h["image_url"] == image_name and h.get("category") == category for h in hoodies):
        raise HTTPException(status_code=404, detail="Image not linked to any hoodie")

    image_path = os.path.join(HOODIE_FOLDER, category, image_name)
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")

    return FileResponse(image_path, media_type="image/png")

@router.post("/hoodies/generate")
async def generate_hoodie():
    category = "generated"
    filename = f"{uuid.uuid4()}.png"
    path = os.path.join(HOODIE_FOLDER, category, filename)

    os.makedirs(os.path.dirname(path), exist_ok=True)  # create folder if not exists

    img = Image.new("RGB", (200, 200), color="green")
    img.save(path)

    # Save metadata
    hoodies = load_hoodies()
    new_hoodie = {
        "id": len(hoodies) + 1,
        "name": f"Hoodie {len(hoodies) + 1}",
        "image_url": filename,
        "category": category,
    }
    hoodies.append(new_hoodie)
    save_hoodies(hoodies)

    return {"message": "New hoodie generated", "filename": filename, "url": f"/hoodies/image/{category}/{filename}"}