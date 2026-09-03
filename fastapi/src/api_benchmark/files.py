from pathlib import Path 
import os

folder = Path(os.environ.get("FILE_DIR", "./files")).resolve()
folder.mkdir(exist_ok=True)

sizes = {
    "file_1kb.txt": 1 * 1024,
    "file_10kb.txt": 10 * 1024,
    "file_1mb.txt": 1 * 1024 * 1024,
    "file_100mb.txt": 100 * 1024 * 1024 ,
}

for filename, size in sizes.items():
    with open(folder / filename, "wb") as f:
        f.write(b"A" * size)


    print(f"{filename}: {size:,} bytes")
