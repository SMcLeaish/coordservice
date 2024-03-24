"""
This module contains the FastAPI application.
"""

import shutil
import uuid
from pathlib import Path

from coordextract import process_coords
from coordextract.point import PointModel
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/process-gpx/")
async def process_gpx(
    file: UploadFile = File(...),
) -> str | list[PointModel] | None:
    """
    Process a GPX file and return the coordinates.
    """
    temp_file = Path(f"temp_{uuid.uuid4()}_{file.filename}")
    with temp_file.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    result = await process_coords(temp_file, indentation=None)
    temp_file.unlink()

    return result
