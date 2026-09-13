from pathlib import Path
import shutil

# Folder to organize
folder = Path("downloads")

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav"],
}

if not folder.exists():
    print(f"Folder '{folder}' does not exist.")
else:
    for file in folder.iterdir():
        if not file.is_file():
            continue

        category = "Others"

        for name, extensions in categories.items():
            if file.suffix.lower() in extensions:
                category = name
                break

        destination = folder / category
        destination.mkdir(exist_ok=True)

        shutil.move(str(file), str(destination / file.name))

    print("✅ Files organized successfully!")