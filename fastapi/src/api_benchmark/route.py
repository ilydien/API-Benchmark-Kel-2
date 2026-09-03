from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import os

router = APIRouter()

FILE_DIR = Path(os.environ.get("FILE_DIR", "./files")).resolve()

@router.get("/files/{filename}")
def serve_file(filename : str): 

    file_path = FILE_DIR / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return FileResponse(
        path=file_path,
        media_type="text/plain",
        filename=filename
    )
