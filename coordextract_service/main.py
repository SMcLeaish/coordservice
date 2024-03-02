import asyncio
import json
import shutil
import uuid
from pathlib import Path

from coordextract import process_coords
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/process-gpx/")
async def process_gpx(file: UploadFile = File(...)):
    temp_file = Path(f"temp_{uuid.uuid4()}_{file.filename}")
    with temp_file.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    result = await process_coords(temp_file, indentation=None)
    temp_file.unlink()

    return result
